import rclpy
from rclpy.node import Node
from std_msgs.msg import ColorRGBA 
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

class DrivingControll(Node):
    def __init__(self):
        super().__init__('driving_controller')
        
        # 기존의 파라미터 설정
        self.declare_parameter('resolution', 0.02)
        self.declare_parameter('robot_radius', 0.3)
        self.declare_parameter('padding', 0.5)
        
        self.resolution = self.get_parameter('resolution').value
        self.robot_radius = self.get_parameter('robot_radius').value
        self.padding = self.get_parameter('padding').value

        #publisher
        self.grid_pub = self.create_publisher(OccupancyGrid, 'grid_map', 10)
        # Marker Publishe
        self.marker_pub = self.create_publisher(MarkerArray, 'waypoint_markers', 10)
        # 웨이포인트 그리드 설정
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
    [0.258858,-1.509031,0.0],[0.238700,-1.918602,0.0],[0.864890,-1.856671,0.0],
    [1.184077,-2.125553,0.0],[1.213830,-2.739862,0.0],[1.453795,-2.745522,0.0],
    [0.888076,-3.123986,0.0],[0.620790,-3.221388,0.0],[ 0.207611,-3.246014,0.0],
    [0.231549,-2.78444,0.0],[0.605831,-2.750030,0.0],[0.615135,-2.225200,0.0],
    ]   
        self.create_timer(1.0, self.publish_markers)
        # X, Y 좌표 추출 및 정렬
        x_coords = sorted(list(set([round(p[0], 4) for p in self.points])))
        y_coords = sorted(list(set([round(p[1], 4) for p in self.points])))
        

        self.grid_points = [(round(x,4), round(y,4), 0.0) for x, y, _ in self.points]
        self.X_LIST = x_coords
        self.Y_LIST = y_coords
    
        # 맵 속성
        self.map_resolution = 1.0
        self.map_origin = (0, 0)
        self.map_data = None
        self.map_width = 0
        self.map_height = 0
        self.map_frame = 'map'
        
        # 그리드맵 초기화
        self.initialize_grid_map()
        
        self.get_logger().info('Navigation Node initialized')
        self.get_logger().info(f'Grid size: {len(self.Y_LIST)} x {len(self.X_LIST)}')

        # 웨이포인트 시퀀스 관리를 위한 변수들 추가
        self.waypoint_sequence = []
        self.current_waypoint_index = 0
        self.is_navigating = False
        
        # 타이머 추가 - 웨이포인트 내비게이션 상태 체크
        self.create_timer(1.0, self.navigation_callback)
        
        # 웨이포인트에서 멈추는 시간 (초)
        self.stop_duration = 3.0

         # 현재 로봇의 위치를 저장할 변수
        self.current_robot_pose = [0.0, 0.0, 0.0]  # [x, y, yaw]
        
        # nav2 초기화
        self.navigator = BasicNavigator()
        self.navigator.waitUntilNav2Active()
        self.get_logger().info('Nav2 is ready!')
        
        #subscriber
        self.goal_pose_sub = self.create_subscription(
        PoseStamped,
        '/goal_pose',
        self.goal_pose_callback,
        10
        )
        self.amcl_pose_sub = self.create_subscription(
            PoseWithCovarianceStamped,
            '/amcl_pose',
            self.amcl_pose_callback,
            10
        )
        self.path_sub = self.create_subscription(
            Path,
            '/plan',  # Nav2 global planner가 발행하는 경로
            self.path_callback,
            10
        )
        self.current_path = None 

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
        
        # 모든 웨이포인트를 회색으로 표시
        for i, point in enumerate(self.points):
            marker = Marker()
            marker.header.frame_id = "map"
            marker.header.stamp = self.get_clock().now().to_msg()
            marker.ns = "waypoints"
            marker.id = i
            marker.type = Marker.SPHERE
            marker.action = Marker.ADD
            
            # 마커 위치 설정
            marker.pose.position.x = point[0]
            marker.pose.position.y = point[1]
            marker.pose.position.z = 0.1  # 바닥에서 살짝 띄움
            
            # 마커 크기 설정
            marker.scale.x = 0.15
            marker.scale.y = 0.15
            marker.scale.z = 0.15
            
            # 기본 색상 설정 (회색)
            marker.color = ColorRGBA(r=0.7, g=0.7, b=0.7, a=0.5)
            
            # 현재 경로에 포함된 웨이포인트인 경우 파란색으로 표시
            if self.waypoint_sequence:
                for wp in self.waypoint_sequence:
                    if abs(point[0] - wp[0]) < 0.01 and abs(point[1] - wp[1]) < 0.01:
                        marker.color = ColorRGBA(r=0.0, g=0.0, b=1.0, a=1.0)
                        marker.scale.x = 0.3  # 크기를 좀 더 크게
                        marker.scale.y = 0.3
                        marker.scale.z = 0.3
                        break
            
            marker_array.markers.append(marker)
            
            # 웨이포인트 번호 텍스트 마커
            text_marker = Marker()
            text_marker.header.frame_id = "map"
            text_marker.header.stamp = self.get_clock().now().to_msg()
            text_marker.ns = "waypoint_labels"
            text_marker.id = i + len(self.points)
            text_marker.type = Marker.TEXT_VIEW_FACING
            text_marker.action = Marker.ADD
            
            # 텍스트 마커 위치 설정
            text_marker.pose.position.x = point[0]
            text_marker.pose.position.y = point[1]
            text_marker.pose.position.z = 0.3
            
            # 텍스트 마커 크기와 내용 설정
            text_marker.scale.z = 0.2
            text_marker.text = str(i + 1)
            
            # 텍스트 마커 색상 설정 (흰색)
            text_marker.color = ColorRGBA(r=1.0, g=1.0, b=1.0, a=1.0)
            
            marker_array.markers.append(text_marker)
        
        # 경로 선 표시
        if self.waypoint_sequence and len(self.waypoint_sequence) > 1:
            line_marker = Marker()
            line_marker.header.frame_id = "map"
            line_marker.header.stamp = self.get_clock().now().to_msg()
            line_marker.ns = "path_line"
            line_marker.id = len(self.points) * 2  # 고유한 ID
            line_marker.type = Marker.LINE_STRIP
            line_marker.action = Marker.ADD
            
            # 선 크기 설정
            line_marker.scale.x = 0.05  # 선 두께
            
            # 선 색상 설정 (녹색)
            line_marker.color = ColorRGBA(r=0.0, g=1.0, b=0.0, a=1.0)
            
            # 경로 포인트 추가
            for point in self.waypoint_sequence:
                p = Point()
                p.x = point[0]
                p.y = point[1]
                p.z = 0.1
                line_marker.points.append(p)
            
            marker_array.markers.append(line_marker)
        
        # 마커 발행
        self.marker_pub.publish(marker_array)
                
        
    def path_callback(self, msg):
        """Nav2 planner가 생성한 경로를 받아서 웨이포인트 설정"""
        self.current_path = msg
        self.get_logger().info('Received new path from planner')
        
        # 경로가 없다면 리턴
        if self.is_navigating:
            return
        self.get_logger().info('Received new path from planner')
        
        if not msg.poses:
            return
        
        # 경로 상의 포인트들을 일정 간격으로 샘플링
        sampled_points = []
        sample_distance = 1.0  # 1미터 간격으로 샘플링
        
        for i in range(0, len(msg.poses), int(sample_distance / 0.05)):  # 0.05는 플래너의 기본 해상도
            pose = msg.poses[i]
            sampled_points.append((pose.pose.position.x, pose.pose.position.y))
        
        # 마지막 포인트 추가
        goal_pose = msg.poses[-1].pose
        goal_point = (goal_pose.position.x, goal_pose.position.y)
        
        # 각 샘플링된 포인트에 대해 가장 가까운 웨이포인트 찾기
        waypoint_sequence = []
        used_waypoints = set()  # 중복 방지를 위한 집합
        
        for point in sampled_points:
            nearest_wp = None
            min_dist = float('inf')
            
            for wp in self.grid_points:
                if wp in used_waypoints:
                    continue
                    
                dist = self.distance(point, wp)
                if dist < min_dist and dist < 1.0:  # 2미터 이내의 가장 가까운 웨이포인트
                    min_dist = dist
                    nearest_wp = wp
            
            if nearest_wp:
                waypoint_sequence.append(nearest_wp)
                used_waypoints.add(nearest_wp)
        final_goal = (goal_point[0], goal_point[1], 0.0)
        
        if waypoint_sequence:
            self.get_logger().info(f'Found {len(waypoint_sequence)} waypoints near the planned path')
            self.waypoint_sequence = waypoint_sequence
            # 마지막에 goal_point 추가
            self.waypoint_sequence.append(final_goal)
            self.current_waypoint_index = 0
            self.is_navigating = True
            
            # 첫 번째 웨이포인트로 이동 시작
            first_point = self.waypoint_sequence[0]
            
            goal_pose = PoseStamped()
            goal_pose.header.frame_id = self.map_frame
            goal_pose.header.stamp = self.navigator.get_clock().now().to_msg()
            goal_pose.pose.position.x = first_point[0]
            goal_pose.pose.position.y = first_point[1]
            
            # 방향 설정
            if len(self.waypoint_sequence) > 1:
                next_point = self.waypoint_sequence[1]
                dx = next_point[0] - first_point[0]
                dy = next_point[1] - first_point[1]
                theta = math.atan2(dy, dx)
                goal_pose.pose.orientation.z = math.sin(theta/2)
                goal_pose.pose.orientation.w = math.cos(theta/2)
            
            self.navigator.goToPose(goal_pose)
            self.get_logger().info(f'Moving to first waypoint: {first_point}')

        
    
    def goal_pose_callback(self, msg):
        """RViz2에서 설정한 Goal Pose 처리"""
        self.get_logger().info('\n=== Received New Goal Pose ===')
        self.get_logger().info(
            f'Position: ({msg.pose.position.x:.2f}, {msg.pose.position.y:.2f})'
        )
            # 이전 내비게이션 상태 초기화
        self.is_navigating = False
        self.waypoint_sequence = []
        self.current_waypoint_index = 0
            # Nav2에 직접 목표점 전달
        self.navigator.goToPose(msg)   

    def amcl_pose_callback(self, msg):
        """AMCL에서 추정된 로봇의 현재 위치 업데이트"""
        self.current_robot_pose[0] = msg.pose.pose.position.x
        self.current_robot_pose[1] = msg.pose.pose.position.y
        
        # 쿼터니언을 yaw로 변환
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
        """주기적으로 내비게이션 상태를 체크하고 다음 웨이포인트로 이동"""
        if not self.is_navigating:
            self.get_logger().debug('Not navigating...')
            return
        
        try:
            current_pose = self.get_current_pose()
            current_waypoint = self.waypoint_sequence[self.current_waypoint_index]
            
            # 현재 위치와 목표 웨이포인트 사이의 거리 계산
            distance_to_waypoint = math.sqrt(
                (current_pose[0] - current_waypoint[0])**2 + 
                (current_pose[1] - current_waypoint[1])**2
            )
            distance_threshold = 0.2
            self.get_logger().info('\n=== Navigation Status ===')
            self.get_logger().info(f'Current Waypoint: {self.current_waypoint_index + 1}/{len(self.waypoint_sequence)}')
            self.get_logger().info(f'AMCL Position: ({current_pose[0]:.4f}, {current_pose[1]:.4f})')
            self.get_logger().info(f'Target Waypoint: ({current_waypoint[0]:.4f}, {current_waypoint[1]:.4f})')
            self.get_logger().info(f'Distance to Waypoint: {distance_to_waypoint:.4f}m')
            
            if self.navigator.isTaskComplete() or distance_to_waypoint < distance_threshold :
                self.get_logger().info('\n=== Waypoint Reached ===')
                self.get_logger().info(f'Waypoint {self.current_waypoint_index + 1} reached!')
                self.get_logger().info(f'AMCL Final Position: ({self.current_robot_pose[0]:.4f}, {self.current_robot_pose[1]:.4f}, {self.current_robot_pose[2]:.4f})')
                self.get_logger().info(f'Target Was: ({current_waypoint[0]:.4f}, {current_waypoint[1]:.4f})')
                self.get_logger().info(f'Position Error: ({abs(self.current_robot_pose[0] - current_waypoint[0]):.4f}, {abs(self.current_robot_pose[1] - current_waypoint[1]):.4f})')
                
                if self.current_waypoint_index < len(self.waypoint_sequence) - 1:
                    self.current_waypoint_index += 1
                    next_point = self.waypoint_sequence[self.current_waypoint_index]
                    
                    goal_pose = PoseStamped()
                    goal_pose.header.frame_id = self.map_frame
                    goal_pose.header.stamp = self.navigator.get_clock().now().to_msg()
                    goal_pose.pose.position.x = next_point[0]
                    goal_pose.pose.position.y = next_point[1]
                    
                    # 방향 설정
                    if self.current_waypoint_index < len(self.waypoint_sequence) - 1:
                        next_next_point = self.waypoint_sequence[self.current_waypoint_index + 1]
                        dx = next_next_point[0] - next_point[0]
                        dy = next_next_point[1] - next_point[1]
                        theta = math.atan2(dy, dx)
                        goal_pose.pose.orientation.z = math.sin(theta/2)
                        goal_pose.pose.orientation.w = math.cos(theta/2)
                    
                    self.get_logger().info(f'Moving to next waypoint: ({next_point[0]:.4f}, {next_point[1]:.4f})')
                    self.navigator.goToPose(goal_pose)
                else:
                    self.get_logger().info('\n=== Navigation Complete ===')
                    self.get_logger().info('Reached final destination!')
                    self.get_logger().info(f'Final AMCL Position: ({self.current_robot_pose[0]:.4f}, {self.current_robot_pose[1]:.4f}, {self.current_robot_pose[2]:.4f})')
                    self.get_logger().info(f'Final Target Was: ({current_waypoint[0]:.4f}, {current_waypoint[1]:.4f})')
                    self.get_logger().info(f'Final Position Error: ({abs(self.current_robot_pose[0] - current_waypoint[0]):.4f}, {abs(self.current_robot_pose[1] - current_waypoint[1]):.4f})')
                    self.is_navigating = False
                    self.current_waypoint_index = 0
                    self.waypoint_sequence = []

        except Exception as e:
            self.get_logger().error(f'Error in navigation_callback: {str(e)}')
    
    def initialize_grid_map(self):
        """그리드맵 초기화"""
        # 맵 크기 계산
        x_min, x_max = min(self.X_LIST), max(self.X_LIST)
        y_min, y_max = min(self.Y_LIST), max(self.Y_LIST)
        
        # 맵 크기를 resolution으로 나누어 그리드 크기 계산
        self.map_width = int((x_max - x_min) / self.resolution) + 1
        self.map_height = int((y_max - y_min) / self.resolution) + 1
        
        # 맵 데이터 초기화 (모든 셀을 빈 공간으로)
        self.map_data = np.ones((self.map_height, self.map_width), dtype=int) * 100
        
        # 그리드 포인트 표시
        for point in self.grid_points:
            grid_x = int((point[0] - x_min) / self.resolution)
            grid_y = int((point[1] - y_min) / self.resolution)
            if 0 <= grid_x < self.map_width and 0 <= grid_y < self.map_height:
                self.map_data[grid_y, grid_x] = 0  # 그리드 포인트 표시
        
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
        # 현재 위치에서 목표점까지의 경로 계산
            current_pose = self.get_current_pose()
            self.get_logger().info(f'Current robot pose: ({current_pose[0]:.4f}, {current_pose[1]:.4f})')
            
            path = self.plan_path(current_pose, (msg.x, msg.y))
            
            if path:
                self.waypoint_sequence = path
                self.current_waypoint_index = 0
                self.is_navigating = True
                
                # 첫 번째 웨이포인트로 이동 시작
                first_point = self.waypoint_sequence[0]
                self.get_logger().info(f'Starting navigation with {len(self.waypoint_sequence)} waypoints')
                
                goal_pose = PoseStamped()
                goal_pose.header.frame_id = self.map_frame
                goal_pose.header.stamp = self.navigator.get_clock().now().to_msg()
                goal_pose.pose.position.x = first_point[0]
                goal_pose.pose.position.y = first_point[1]
                
                # 방향 설정
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