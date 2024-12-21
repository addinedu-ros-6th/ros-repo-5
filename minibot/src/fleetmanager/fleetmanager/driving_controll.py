import rclpy
from rclpy.node import Node
from std_msgs.msg import ColorRGBA , Empty
from nav_msgs.msg import OccupancyGrid,Path
from nav2_msgs.msg import Costmap
from geometry_msgs.msg import PoseStamped, Point ,Twist
from nav2_simple_commander.robot_navigator import BasicNavigator
from visualization_msgs.msg import Marker, MarkerArray
from rclpy.duration import Duration
import os
import numpy as np
import math
from geometry_msgs.msg import PoseWithCovarianceStamped
import time
from fleetmanger_msgs.srv import DrivingStatus
from fleetmanger_msgs.msg import WaypointStatus
from builtin_interfaces.msg import Time  

 


class DrivingControll(Node):
    def __init__(self):
        super().__init__('driving_controller')
        
        

        self.domain_id = int(os.environ.get('ROS_DOMAIN_ID')) 
        if self.domain_id == 90:
            self.robot_name = 'robot0'
            self.other_robot_name = 'robot1'
        elif self.domain_id == 91:
            self.robot_name = 'robot1'
            self.other_robot_name = 'robot0'
        self.get_logger().info(f'Initializing {self.robot_name} on domain {self.domain_id}')
        # 기존의 파라미터 설정
        self.declare_parameter('resolution', 0.02)
        self.declare_parameter('robot_radius', 0.25)
        self.declare_parameter('padding', 0.2)
        
        self.resolution = self.get_parameter('resolution').value
        self.robot_radius = self.get_parameter('robot_radius').value
        self.padding = self.get_parameter('padding').value

        self.last_position = None
        self.stationary_start_time = None
        self.stationary_threshold = 1.5  # 정지 상태로 판단할 시간 (초)
        self.position_threshold = 0.01  
     
        self.original_start_time = Time(sec=0, nanosec=0)
        self.navigation_start_time = Time(sec=0, nanosec=0) 

        self.status_sent = False
        self.drive_status_client = self.create_client(DrivingStatus, 'DrivingStatus')

        #publisher
        self.grid_pub = self.create_publisher(OccupancyGrid, 'grid_map', 10)
     
        self.marker_pub = self.create_publisher(MarkerArray, 'waypoint_markers', 10)
        self.goal_reached_pub = self.create_publisher(Empty, '/goal_reached', 10)
     
        self.points = [
            [1.340028, -0.003381, 0.0],  # trash1
            [0.840462, -0.739715, 0.0],  # trash2
            [0.779708, -1.262948, 0.0],  # trash3
            [0.248580, -2.396516, 0.0],  # trash4
            [1.251284, -3.195752, 0.0],  # trash5
            [1.417877, -2.101801, 0.0],  # trash6
            [0.252721, -0.999474, 0.0],[1.410261,-0.944804,0.0],[1.374446,-0.40111,0.0],
            [0.800220,-0.401572,0.0],[0.796630,-0.013749,0.0],[0.274894,-0.001018,0.0],
            [0.235932,-0.520341,0.0],[1.432302,-1.478842,0.0],
            [0.258858,-1.409031,0.0],[0.238700,-1.918602,0.0],[0.864890,-1.856671,0.0],
            [1.184077,-2.125553,0.0],[1.213830,-2.739862,0.0],[1.453795,-2.745522,0.0],
            [0.888076,-3.123986,0.0],[0.620790,-3.221388,0.0],[ 0.207611,-3.246014,0.0],
            [0.231549,-2.78444,0.0],[0.605831,-2.750030,0.0],[0.615135,-2.225200,0.0],
            ]   
        self.create_timer(1.0, self.publish_markers)

        x_coords = sorted(list(set([round(p[0], 4) for p in self.points])))
        y_coords = sorted(list(set([round(p[1], 4) for p in self.points])))
        

        self.grid_points = [(round(x,4), round(y,4), 0.0) for x, y, _ in self.points]
        self.X_LIST = x_coords
        self.Y_LIST = y_coords

        self.map_resolution = self.resolution
        self.map_origin = (0, 0)
        self.map_data = None
        self.map_width = 0
        self.map_height = 0
        self.map_frame = 'map'
        

        self.initialize_grid_map()
        
        self.get_logger().info('Navigation Node initialized')
        self.get_logger().info(f'Grid size: {len(self.Y_LIST)} x {len(self.X_LIST)}')

        
        self.waypoint_sequence = []
        self.current_waypoint_index = 0
        self.is_navigating = False
        
        
        self.create_timer(1.0, self.navigation_callback)
        
        
        self.stop_duration = 3.0

       
        self.current_robot_pose = [0.0, 0.0, 0.0]  # [x, y, yaw]
        
        # nav2 초기화
        self.navigator = BasicNavigator()
        self.navigator.waitUntilNav2Active()
        self.get_logger().info('Nav2 is ready!')
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.amcl_pose_sub = self.create_subscription(
            PoseWithCovarianceStamped,
            '/amcl_pose',
            self.amcl_pose_callback,
            10
        )
        self.path_sub = self.create_subscription(
            Path,
            '/plan', 
            self.path_callback,
            10
        )
        self.current_path = None 
   
       
        self.path_pub = self.create_publisher(
            Path,
            f'{self.robot_name}/path',  
            10
        )
        self.waypoint_status_pub = self.create_publisher(
            WaypointStatus,
            f'{self.robot_name}/waypoint_status',
            10
        )
        self.other_path_sub = self.create_subscription(
            Path,
            f'{self.other_robot_name}/path',
            self.other_robot_path_callback,
            10
        )

        self.other_waypoint_sub = self.create_subscription(
            WaypointStatus,
            f'{self.other_robot_name}/waypoint_status',
            self.other_waypoint_callback,
            10
        )
        self.create_timer(0.5, self.publish_waypoint_status)
        
        self.other_robot_waypoints = None
        

    def check_waypoint_conflict(self):
        """웨이포인트 충돌 감지"""
        if not self.other_robot_waypoints or not self.waypoint_sequence or not self.is_navigating:
            return False, None
                
       
        current_pos = self.get_current_pose()
        
       
        current_wp = self.waypoint_sequence[self.current_waypoint_index]
        
      
        if not self.other_robot_waypoints.is_navigating:
            return False, None

        # 상세 로깅
        self.get_logger().info(
            f'\n=== 충돌 감지 상세 정보 ===\n'
            f'내 로봇: {self.robot_name}\n'
            f'현재 위치: ({current_pos[0]:.4f}, {current_pos[1]:.4f})\n'
            f'목표 위치: ({current_wp[0]:.4f}, {current_wp[1]:.4f})\n'
            f'다른 로봇: {self.other_robot_name}\n'
            f'이동 중: {self.other_robot_waypoints.is_navigating}\n'
            f'웨이포인트 진행도: {self.other_robot_waypoints.current_waypoint_index + 1}/{self.other_robot_waypoints.total_waypoints}'
        )

    
        other_current_wp_idx = self.other_robot_waypoints.current_waypoint_index
        other_robot_target = (
            self.other_robot_waypoints.waypoint_x[other_current_wp_idx],
            self.other_robot_waypoints.waypoint_y[other_current_wp_idx]
        )
        robot_distance = math.sqrt(
            (current_pos[0] - other_robot_target[0])**2 + 
            (current_pos[1] - other_robot_target[1])**2
        )
   
        safety_distance = 0.45
        
        if robot_distance < safety_distance:
            for i in range(len(self.waypoint_sequence) - 1):
                for j in range(len(self.other_robot_waypoints.waypoint_x) - 1):
                    if self.check_path_intersection(
                        self.waypoint_sequence[i],
                        self.waypoint_sequence[i + 1],
                        (self.other_robot_waypoints.waypoint_x[j], 
                        self.other_robot_waypoints.waypoint_y[j]),
                        (self.other_robot_waypoints.waypoint_x[j + 1],
                        self.other_robot_waypoints.waypoint_y[j + 1])
                    ):
                        self.get_logger().warn(
                            f'\n=== 경로 교차 감지! ===\n'
                            f'내 경로: ({self.waypoint_sequence[i][0]:.4f}, {self.waypoint_sequence[i][1]:.4f}) -> '
                            f'({self.waypoint_sequence[i + 1][0]:.4f}, {self.waypoint_sequence[i + 1][1]:.4f})\n'
                            f'다른 로봇 경로: ({self.other_robot_waypoints.waypoint_x[j]:.4f}, '
                            f'{self.other_robot_waypoints.waypoint_y[j]:.4f}) -> '
                            f'({self.other_robot_waypoints.waypoint_x[j + 1]:.4f}, '
                            f'{self.other_robot_waypoints.waypoint_y[j + 1]:.4f})'
                        )
                        
                        if (self.original_start_time and self.other_robot_waypoints.start_time):
                            my_start_sec = float(self.original_start_time.sec) + float(self.original_start_time.nanosec) / 1e9
                            other_start_sec = float(self.other_robot_waypoints.start_time.sec) + float(self.other_robot_waypoints.start_time.nanosec) / 1e9
                            
                            self.get_logger().warn(
                                f'\n=== 시작 시간 비교 ===\n'
                                f'{self.robot_name}: {my_start_sec:.4f}초\n'
                                f'{self.other_robot_name}: {other_start_sec:.4f}초\n'
                                f'차이: {abs(my_start_sec - other_start_sec):.4f}초'
                            )
                            
                            if my_start_sec > other_start_sec:
                                return True, "wait"
                            else:
                                avoidance_wp = self.find_avoidance_waypoint(
                                    (self.other_robot_waypoints.waypoint_x[j],
                                    self.other_robot_waypoints.waypoint_y[j])
                                )
                                if avoidance_wp:
                                    return True, ("reroute", avoidance_wp)
        
        return False, None
    def check_path_intersection(self, p1, p2, p3, p4):
        """두 경로(선분)가 교차하는지 확인"""
        def ccw(A, B, C):
            return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])
        
        A = (p1[0], p1[1])
        B = (p2[0], p2[1])
        C = (p3[0], p3[1])
        D = (p4[0], p4[1])
        
        return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
    

    def find_avoidance_waypoint(self, obstacle_wp):
        """충돌을 피하기 위한 우회 웨이포인트 찾기"""
        best_waypoint = None
        min_cost = float('inf')
        safe_distance = 0.4  
        
        for wp in self.grid_points:
          
            distance_to_obstacle = math.sqrt(
                (wp[0] - obstacle_wp[0])**2 + 
                (wp[1] - obstacle_wp[1])**2
            )
            
          
            distance_to_path = min(
                math.sqrt((wp[0] - p[0])**2 + (wp[1] - p[1])**2)
                for p in self.waypoint_sequence
            )
            
            
            if distance_to_obstacle > safe_distance:
                cost = distance_to_path + (1.0 / distance_to_obstacle)
                if cost < min_cost:
                    min_cost = cost
                    best_waypoint = wp
        
        return best_waypoint


    def publish_waypoint_status(self):
        """현재 로봇의 waypoint 상태를 발행"""
        if hasattr(self, 'waypoint_sequence'):
            msg = WaypointStatus()
            msg.robot_id = self.robot_name
            msg.current_waypoint_index = self.current_waypoint_index
            msg.total_waypoints = len(self.waypoint_sequence)
            msg.waypoint_x = [p[0] for p in self.waypoint_sequence]
            msg.waypoint_y = [p[1] for p in self.waypoint_sequence]
            msg.is_navigating = self.is_navigating
            
            msg.start_time = self.original_start_time
            
            self.waypoint_status_pub.publish(msg)
    def other_robot_path_callback(self, msg):
        """다른 로봇의 경로를 받았을 때 처리하는 콜백"""
        self.other_robot_path = msg
        self.get_logger().info(
            f'Received path from {self.other_robot_name} with {len(msg.poses)} poses'
        )

    def other_waypoint_callback(self, msg):
        """다른 로봇의 waypoint 상태를 받았을 때 처리하는 콜백"""
        self.other_robot_waypoints = msg
      

    def publish_cmd_vel(self, linear_x, angular_z, duration):
        """cmd_vel 발행하는 함수"""
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        
   
        self.get_logger().info(f'\n=== Publishing Velocity Command ===')
        self.get_logger().info(f'Linear velocity: {linear_x} m/s')
        self.get_logger().info(f'Angular velocity: {angular_z} rad/s')
        self.get_logger().info(f'Duration: {duration} seconds')
        
   
        start_time = self.get_clock().now()
        end_time = start_time + Duration(seconds=duration)
        
        
        while self.get_clock().now() <= end_time:
            self.cmd_vel_pub.publish(msg)
            time.sleep(0.1) 
        
     
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.cmd_vel_pub.publish(msg)
        
        
        self.get_logger().info('Velocity command completed')
        
   
        if self.current_waypoint_index < len(self.waypoint_sequence) - 1:
            self.current_waypoint_index += 1
            next_point = self.waypoint_sequence[self.current_waypoint_index]
            
            goal_pose = PoseStamped()
            goal_pose.header.frame_id = self.map_frame
            goal_pose.header.stamp = self.navigator.get_clock().now().to_msg()
            goal_pose.pose.position.x = next_point[0]
            goal_pose.pose.position.y = next_point[1]
          
            if self.current_waypoint_index < len(self.waypoint_sequence) - 1:
                next_next_point = self.waypoint_sequence[self.current_waypoint_index + 1]
                dx = next_next_point[0] - next_point[0]
                dy = next_next_point[1] - next_point[1]
                theta = math.atan2(dy, dx)
                goal_pose.pose.orientation.z = math.sin(theta/2)
                goal_pose.pose.orientation.w = math.cos(theta/2)
            
            self.get_logger().info(f'Moving to next waypoint: ({next_point[0]:.4f}, {next_point[1]:.4f})')
            self.navigator.goToPose(goal_pose)
    
    def send_request(self, status):
        request = DrivingStatus.Request()
      
        request.driving_status = status

        future = self.drive_status_client.call_async(request)
        future.add_done_callback(self.handle_job_complete)
        

    def handle_job_complete(self, future):
        response = future.result()
        self.get_logger().info(f"Response received: {response}")

    
    def get_line_points(self, start, end, num_points=20):
        """두 점 사이의 직선 상의 점들을 반환"""
        points = []
        for i in range(num_points):
            t = i / (num_points - 1)
            x = start[0] + t * (end[0] - start[0])
            y = start[1] + t * (end[1] - start[1])
            points.append((x, y))
        return points
    
    def publish_markers(self):
        """웨이포인트를 RViz2에서 볼 수 있도록 마커로 발행"""
        marker_array = MarkerArray()
        
    
        for i, point in enumerate(self.points):
            marker = Marker()
            marker.header.frame_id = "map"
            marker.header.stamp = self.get_clock().now().to_msg()
            marker.ns = "waypoints"
            marker.id = i
            marker.type = Marker.SPHERE
            marker.action = Marker.ADD
            
          
            marker.pose.position.x = point[0]
            marker.pose.position.y = point[1]
            marker.pose.position.z = 0.1  
            
        
            marker.scale.x = 0.15
            marker.scale.y = 0.15
            marker.scale.z = 0.15
            
         
            marker.color = ColorRGBA(r=0.7, g=0.7, b=0.7, a=0.5)
            
            if self.waypoint_sequence:
                for wp in self.waypoint_sequence:
                    if abs(point[0] - wp[0]) < 0.01 and abs(point[1] - wp[1]) < 0.01:
                        marker.color = ColorRGBA(r=0.0, g=0.0, b=1.0, a=1.0)
                        marker.scale.x = 0.3
                        marker.scale.y = 0.3
                        marker.scale.z = 0.3
                        break
            
            marker_array.markers.append(marker)
            
           
            text_marker = Marker()
            text_marker.header.frame_id = "map"
            text_marker.header.stamp = self.get_clock().now().to_msg()
            text_marker.ns = "waypoint_labels"
            text_marker.id = i + len(self.points)
            text_marker.type = Marker.TEXT_VIEW_FACING
            text_marker.action = Marker.ADD
            
            text_marker.pose.position.x = point[0]
            text_marker.pose.position.y = point[1]
            text_marker.pose.position.z = 0.3
            
            
            text_marker.scale.z = 0.2
            text_marker.text = str(i + 1)
            
            
            text_marker.color = ColorRGBA(r=1.0, g=1.0, b=1.0, a=1.0)
            
            marker_array.markers.append(text_marker)
     
        if self.waypoint_sequence and len(self.waypoint_sequence) > 1:
            line_marker = Marker()
            line_marker.header.frame_id = "map"
            line_marker.header.stamp = self.get_clock().now().to_msg()
            line_marker.ns = "path_line"
            line_marker.id = len(self.points) * 2  
            line_marker.type = Marker.LINE_STRIP
            line_marker.action = Marker.ADD
            
           
            line_marker.scale.x = 0.05  # 선 두께
            
         
            line_marker.color = ColorRGBA(r=0.0, g=1.0, b=0.0, a=1.0)
            
           
            for point in self.waypoint_sequence:
                p = Point()
                p.x = point[0]
                p.y = point[1]
                p.z = 0.1
                line_marker.points.append(p)
            
            marker_array.markers.append(line_marker)
        
     
        self.marker_pub.publish(marker_array)


        
    def path_callback(self, msg):
        """Nav2 planner가 생성한 경로를 받아서 웨이포인트 설정"""
        self.current_path = msg
        self.get_logger().info('Received new path from planner')
       
        
        if self.is_navigating:
            return
        
        
        if not msg.poses:
            return
        
        if self.is_navigating:
            self.get_logger().info('Canceling current navigation task...')
            self.navigator.cancelTask()
            self.is_navigating = False 
            time.sleep(0.5)

        current_time = self.get_clock().now().to_msg()
        self.navigation_start_time = Time(
        sec=current_time.sec,
        nanosec=current_time.nanosec
    )
        self.original_start_time = Time(
        sec=current_time.sec,
        nanosec=current_time.nanosec
    )
        self.get_logger().warn(f'Start_time :{self.navigation_start_time}')
        
        # 경로 상의 포인트들을 일정 간격으로 샘플링
        sampled_points = []
        sample_distance = 1.1
        
        for i in range(0, len(msg.poses), int(sample_distance / 0.05)):  
            pose = msg.poses[i]
            sampled_points.append((pose.pose.position.x, pose.pose.position.y))
        
       
        goal_pose = msg.poses[-1].pose
        goal_point = (goal_pose.position.x, goal_pose.position.y)
        
        
        waypoint_sequence = []
        used_waypoints = set()  
        
        for point in sampled_points:
            nearest_wp = None
            min_dist = float('inf')
            
            for wp in self.grid_points:
                if wp in used_waypoints:
                    continue
                    
                dist = self.distance(point, wp)
                if dist < min_dist and dist < 0.8:  
                    min_dist = dist
                    nearest_wp = wp
            
            if nearest_wp:
                waypoint_sequence.append(nearest_wp)
                used_waypoints.add(nearest_wp)
        final_goal = (goal_point[0], goal_point[1], 0.0)
        
        if waypoint_sequence:
            self.get_logger().info(f'Found {len(waypoint_sequence)} waypoints near the planned path')
            self.waypoint_sequence = waypoint_sequence
            self.waypoint_sequence.append(final_goal)
            self.current_waypoint_index = 0
            self.is_navigating = True
            self.status_sent = False 
      
            first_point = self.waypoint_sequence[0]
            
            goal_pose = PoseStamped()
            goal_pose.header.frame_id = self.map_frame
            goal_pose.header.stamp = self.navigator.get_clock().now().to_msg()
            goal_pose.pose.position.x = first_point[0]
            goal_pose.pose.position.y = first_point[1]

            if len(self.waypoint_sequence) > 1:
                next_point = self.waypoint_sequence[1]
                dx = next_point[0] - first_point[0]
                dy = next_point[1] - first_point[1]
                theta = math.atan2(dy, dx)
                goal_pose.pose.orientation.z = math.sin(theta/2)
                goal_pose.pose.orientation.w = math.cos(theta/2)
            
            self.navigator.goToPose(goal_pose)
            self.get_logger().info(f'Moving to first waypoint: {first_point}')

    def amcl_pose_callback(self, msg):
        """AMCL에서 추정된 로봇의 현재 위치 업데이트"""
        self.current_robot_pose[0] = msg.pose.pose.position.x
        self.current_robot_pose[1] = msg.pose.pose.position.y
        
        
        orientation = msg.pose.pose.orientation
        _, _, yaw = self.euler_from_quaternion(
            orientation.x,
            orientation.y,
            orientation.z,
            orientation.w
        )
        self.current_robot_pose[2] = yaw

    def euler_from_quaternion(self, x, y, z, w):
        """쿼터니언을 오일러 각으로 변환"""
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)

        return roll_x, pitch_y, yaw_z

    def get_current_pose(self):
        """현재 로봇의 위치 반환"""
        return (self.current_robot_pose[0], self.current_robot_pose[1])

    def navigation_callback(self):
        """주기적으로 내비게이션 상태를 체크하고 웨이포인트 도달을 감지"""
        if not self.is_navigating or not hasattr(self, 'waypoint_sequence') or not self.waypoint_sequence:
            return
        
        try:
            self.get_logger().info(
            f'\n=== 충돌 감지 체크 시작 ===\n'
            f'로봇: {self.robot_name}\n'
            f'다른 로봇 정보 존재: {self.other_robot_waypoints is not None}\n'
            f'현재 웨이포인트 인덱스: {self.current_waypoint_index}\n'
            f'총 웨이포인트 수: {len(self.waypoint_sequence)}'
            )

            should_modify, action = self.check_waypoint_conflict()
            if should_modify:
                if action == "wait":
                    
                    self.get_logger().info('웨이포인트 충돌 방지를 위해 대기 중...')
                    self.navigator.cancelTask()

                    my_start_sec = float(self.original_start_time.sec) + float(self.original_start_time.nanosec) / 1e9
                    other_start_sec = float(self.other_robot_waypoints.start_time.sec) + float(self.other_robot_waypoints.start_time.nanosec) / 1e9
                    self.get_logger().warn(
                        f'\n=== 시작 시간 비교 ===\n'
                        f'{self.robot_name}: {my_start_sec:.4f}초\n'
                        f'{self.other_robot_name}: {other_start_sec:.4f}초\n'
                        f'차이: {abs(my_start_sec - other_start_sec):.4f}초'
                    )

                    
                    current_pose = self.get_current_pose()
                    current_target = self.waypoint_sequence[self.current_waypoint_index]
                 
                    collision_detected = False
                    for i in range(len(self.other_robot_waypoints.waypoint_x) - 1):
                        if self.check_path_intersection(
                            current_pose,
                            current_target,
                            (self.other_robot_waypoints.waypoint_x[i],
                            self.other_robot_waypoints.waypoint_y[i]),
                            (self.other_robot_waypoints.waypoint_x[i + 1],
                            self.other_robot_waypoints.waypoint_y[i + 1])
                        ):
                            collision_detected = True
                            break
                    
                    
                    if not collision_detected:
                        goal_pose = PoseStamped()
                        goal_pose.header.frame_id = self.map_frame
                        goal_pose.header.stamp = self.navigator.get_clock().now().to_msg()
                        goal_pose.pose.position.x = current_target[0]
                        goal_pose.pose.position.y = current_target[1]
                        
                    
                        if self.current_waypoint_index + 1 < len(self.waypoint_sequence):
                            next_wp = self.waypoint_sequence[self.current_waypoint_index + 1]
                            dx = next_wp[0] - current_target[0]
                            dy = next_wp[1] - current_target[1]
                            theta = math.atan2(dy, dx)
                            goal_pose.pose.orientation.z = math.sin(theta/2)
                            goal_pose.pose.orientation.w = math.cos(theta/2)
                        
                        self.navigator.goToPose(goal_pose)
                        self.get_logger().info(f'충돌 위험이 감소하여 경로 재개: ({current_target[0]:.4f}, {current_target[1]:.4f})')
                    
                    return
                elif isinstance(action, tuple) and action[0] == "reroute":
                    avoidance_wp = action[1]
                    self.get_logger().warn(
                        f'\n=== 충돌 회피 동작: 우회 ===\n'
                        f'로봇: {self.robot_name}\n'
                        f'우회 지점: ({avoidance_wp[0]:.4f}, {avoidance_wp[1]:.4f})'
                    )
                    
              
                    self.navigator.cancelTask()
                    
                    self.waypoint_sequence.insert(
                        self.current_waypoint_index + 1,
                        (avoidance_wp[0], avoidance_wp[1], 0.0)
                    )
                    self.get_logger().info(f'우회 웨이포인트 추가됨: ({avoidance_wp[0]:.4f}, {avoidance_wp[1]:.4f})')
                    
                  
                    goal_pose = PoseStamped()
                    goal_pose.header.frame_id = self.map_frame
                    goal_pose.header.stamp = self.navigator.get_clock().now().to_msg()
                    goal_pose.pose.position.x = avoidance_wp[0]
                    goal_pose.pose.position.y = avoidance_wp[1]
                    
                    self.navigator.goToPose(goal_pose)
                    return



            current_pose = self.get_current_pose()
            current_waypoint = self.waypoint_sequence[self.current_waypoint_index]
            
            
            distance_to_waypoint = math.sqrt(
                (current_pose[0] - current_waypoint[0])**2 + 
                (current_pose[1] - current_waypoint[1])**2
            )
            distance_threshold = 0.3
            
            current_yaw = self.current_robot_pose[2]
            target_yaw = current_yaw  
        
            angle_diff = math.atan2(math.sin(target_yaw - current_yaw), 
                                  math.cos(target_yaw - current_yaw))
            angle_threshold = 0.2  
            
            if self.last_position is None:
                self.last_position = current_pose
                self.stationary_start_time = self.get_clock().now()
            else:
                
                position_change = math.sqrt(
                    (current_pose[0] - self.last_position[0])**2 +
                    (current_pose[1] - self.last_position[1])**2
                )
                
                current_time = self.get_clock().now()
                if position_change < self.position_threshold:
              
                    if self.stationary_start_time is None:
                        self.stationary_start_time = current_time
                    else:
                            
                            time_diff = (current_time - self.stationary_start_time).to_msg().sec
                            if time_diff > self.stationary_threshold:
                                self.get_logger().info('\n=== Robot Stationary Detected ===')
                                self.get_logger().info(f'Robot has not moved significantly for {self.stationary_threshold} seconds')
                                self.get_logger().info('Executing recovery movement...')
                                self.publish_cmd_vel(0.05, 0.0, 0.5)  
                                self.stationary_start_time = None  
                else:
                        self.stationary_start_time = None
                
                self.last_position = current_pose
            
            
            
            self.get_logger().info('\n=== Navigation Status ===')
            self.get_logger().info(f'Current Waypoint: {self.current_waypoint_index + 1}/{len(self.waypoint_sequence)}')
            self.get_logger().info(f'AMCL Position: ({current_pose[0]:.4f}, {current_pose[1]:.4f})')
            self.get_logger().info(f'Target Waypoint: ({current_waypoint[0]:.4f}, {current_waypoint[1]:.4f})')
            self.get_logger().info(f'Distance to Waypoint: {distance_to_waypoint:.4f}m')
            

            if self.navigator.isTaskComplete() or distance_to_waypoint < distance_threshold:
                self.get_logger().info('\n=== Waypoint Reached ===')
                self.get_logger().info(f'Waypoint {self.current_waypoint_index + 1} reached!')
                self.get_logger().info(f'AMCL Final Position: ({self.current_robot_pose[0]:.4f}, {self.current_robot_pose[1]:.4f}, {self.current_robot_pose[2]:.4f})')
                self.get_logger().info(f'Target Was: ({current_waypoint[0]:.4f}, {current_waypoint[1]:.4f})')
                self.get_logger().info(f'Position Error: ({abs(self.current_robot_pose[0] - current_waypoint[0]):.4f}, {abs(self.current_robot_pose[1] - current_waypoint[1]):.4f})')

                if self.current_waypoint_index == len(self.waypoint_sequence) - 1:
                    self.get_logger().info('\n=== Navigation Complete ===')
                    self.get_logger().info('Robot has reached the final destination!')
                    self.get_logger().info(f'Total waypoints visited: {len(self.waypoint_sequence)}')
                    self.get_logger().info(f'Final position: ({self.current_robot_pose[0]:.4f}, {self.current_robot_pose[1]:.4f}, {self.current_robot_pose[2]:.4f})')
                    
                    if abs(angle_diff) > angle_threshold:
                        angular_speed = 0.3 if angle_diff > 0 else -0.3
                        self.publish_cmd_vel(0.0, angular_speed, 0.5)
                    else:
                        self.is_navigating = False
                        self.goal_reached_pub = self.create_publisher(Empty, '/goal_reached', 10)
                        self.navigator.cancelTask()
                        self.navigation_start_time = Time(sec=0, nanosec=0)
                        self.original_start_time = Time(sec=0, nanosec=0)
                        
                        if not self.status_sent:
                            self.send_request(status="driving success")
                            self.status_sent = True
                            self.get_logger().warn('driving_success send')
              

        except Exception as e:

            self.get_logger().error(f'Error in navigation_callback: {str(e)}')
    def initialize_grid_map(self):
        """그리드맵 초기화"""

        x_min, x_max = min(self.X_LIST), max(self.X_LIST)
        y_min, y_max = min(self.Y_LIST), max(self.Y_LIST)
   
        self.map_width = int((x_max - x_min) / self.resolution) + 1
        self.map_height = int((y_max - y_min) / self.resolution) + 1
        
       
        self.map_data = np.ones((self.map_height, self.map_width), dtype=int) * 100
        

        for point in self.grid_points:
            grid_x = int((point[0] - x_min) / self.resolution)
            grid_y = int((point[1] - y_min) / self.resolution)
            if 0 <= grid_x < self.map_width and 0 <= grid_y < self.map_height:
                self.map_data[grid_y, grid_x] = 0  
        
        self.publish_grid_map()

    def publish_grid_map(self):
        """그리드맵 발행"""
        grid_msg = OccupancyGrid()
        grid_msg.header.frame_id = self.map_frame
        grid_msg.header.stamp = self.get_clock().now().to_msg()
        
        grid_msg.info.resolution = self.resolution
        grid_msg.info.width = self.map_width
        grid_msg.info.height = self.map_height
        grid_msg.info.origin.position.x = min(self.X_LIST)
        grid_msg.info.origin.position.y = min(self.Y_LIST)
        grid_msg.info.origin.position.z = 0.0
        
        grid_msg.data = self.map_data.flatten().tolist()
        self.grid_pub.publish(grid_msg)

    def waypoint_callback(self, msg):
        """웨이포인트 메시지 수신 시 처리"""
        self.get_logger().info(f'\n=== New Waypoint Request ===')
        self.get_logger().info(f'Target waypoint: ({msg.x:.4f}, {msg.y:.4f})')
        try:
        
            current_pose = self.get_current_pose()
            self.get_logger().info(f'Current robot pose: ({current_pose[0]:.4f}, {current_pose[1]:.4f})')
            
            path = self.plan_path(current_pose, (msg.x, msg.y))
            
            if path:
                self.waypoint_sequence = path
                self.current_waypoint_index = 0
                self.is_navigating = True
                
                
                first_point = self.waypoint_sequence[0]
                self.get_logger().info(f'Starting navigation with {len(self.waypoint_sequence)} waypoints')
                
                goal_pose = PoseStamped()
                goal_pose.header.frame_id = self.map_frame
                goal_pose.header.stamp = self.navigator.get_clock().now().to_msg()
                goal_pose.pose.position.x = first_point[0]
                goal_pose.pose.position.y = first_point[1]
                
               
                if len(self.waypoint_sequence) > 1:
                    next_point = self.waypoint_sequence[1]
                    dx = next_point[0] - first_point[0]
                    dy = next_point[1] - first_point[1]
                    theta = math.atan2(dy, dx)
                    goal_pose.pose.orientation.z = math.sin(theta/2)
                    goal_pose.pose.orientation.w = math.cos(theta/2)
                
                self.navigator.goToPose(goal_pose)
                self.get_logger().info(f'Moving to first waypoint: {first_point}')
            else:
                self.get_logger().error('Failed to find valid path to goal')
        except Exception as e:
            self.get_logger().error(f'Error in waypoint_callback: {str(e)}')

    def distance(self, point1, point2):
        """두 점 사이의 유클리드 거리 계산"""
        return math.sqrt(
            (point1[0] - point2[0])**2 + 
            (point1[1] - point2[1])**2
        )
    def find_nearest_grid_point(self, x, y):
        """가장 가까운 그리드 포인트 찾기"""
        min_dist = float('inf')
        nearest_point = None
        grid_points_list = list(self.grid_points)
        for point in grid_points_list:
            dist = (point[0] - x)**2 + (point[1] - y)**2
            if dist < min_dist:
                min_dist = dist
                nearest_point = point

        return nearest_point
def main(args=None):
    rclpy.init(args=args)
    navigator = DrivingControll()
    
    try:
        rclpy.spin(navigator)
    except KeyboardInterrupt:
        pass
    finally:
        navigator.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()