import rclpy as rp
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from threading import Event
import threading
import time

from geometry_msgs.msg import Twist
from taskmanager_msgs.srv import JobAllocated, JobCompleteReq
from taskmanager_msgs.msg import RobotStatus
from minibot_interfaces.srv import Pickup
from minibot_interfaces.msg import DeviceData
from camera_interface.msg import YoloDetect
from camera_interface.srv import BasketInfo, PosCalibration
from fleetmanger_msgs.srv import DrivingStatus
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult

class SharedState:
    """로봇 상태를 공유하기 위한 클래스"""
    def __init__(self):
        self.robot_status = "idle"
        self.robot_pose_x = 0.0
        self.robot_pose_y = 0.0
        self.battery_status = 100


class RobotStatusPublisher(Node):
	
    def __init__(self, shared_state):
        super().__init__('RobotStatus_Publisher')
        self.shared_state = shared_state 
        self.publisher = self.create_publisher(RobotStatus, 'RobotStatus', 10)
        self.subscription = self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose', self.pose_callback, 10)

        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.status_callback)
        
        self.robot_pose_x = 0.0
        self.robot_pose_y = 0.0
        self.battery_status = 100
        self.battery_time = 0

    def pose_callback(self, msg):
        self.robot_pose_x = msg.pose.pose.position.x
        self.robot_pose_y = msg.pose.pose.position.y
        # SharedState에 위치 값 동기화
        self.shared_state.robot_pose_x = self.robot_pose_x
        self.shared_state.robot_pose_y = self.robot_pose_y

    def status_callback(self):
        msg = RobotStatus()
        self.battery_time += 0.5

        if self.battery_time > 100:
            if self.battery_status > 0:  # 배터리가 0 이하로 내려가지 않도록
                self.battery_status -= 1
            msg.battery_status = self.battery_status
            self.battery_time = 0
        else: 
            msg.battery_status = self.battery_status

        msg.robot_status = self.shared_state.robot_status
        msg.x = self.robot_pose_x
        msg.y = self.robot_pose_y

        self.publisher.publish(msg)


class JobAllocatedServer(Node):

    def __init__(self, shared_state):
        super().__init__('JobAllocated_server')
        self.shared_state = shared_state
        self.callback_group = ReentrantCallbackGroup()
        self.nav = BasicNavigator()

        # 작업 받는 서버
        self.joballocate_server = self.create_service(JobAllocated, 'JobAllocatedRes', self.allocatd_job, callback_group=self.callback_group)
        # 주행 상태 받는 서버
        self.driving_status_server = self.create_service(DrivingStatus, 'DrivingStatus', self.drivingStatus_server, callback_group=self.callback_group)
        # 작업 완료 클라이언트
        self.jobcomplete_client = self.create_client(JobCompleteReq, 'JobCompleteReq', callback_group=self.callback_group)
        # 픽업 동작 요청 클라이언트
        self.Pickup_client = self.create_client(Pickup, 'PickupServer', callback_group=self.callback_group)
        # 아루코 동작 요청 클라이언트
        self.Aruco_client = self.create_client(BasketInfo, 'basket_data', callback_group=self.callback_group)
        # 아루코 동작 완료 서버
        self.Aruco_server = self.create_service(PosCalibration, 'poscal_data', self.aruco_done, callback_group=self.callback_group)
        # yolo 결과 값 구독
        self.yolo_subscription = self.create_subscription(YoloDetect, 'yolo_detect', self.yolo_callback, 10, callback_group=self.callback_group)
        # 버튼 및 근접센서 값 구독
        self.detected_sensor_subscription = self.create_subscription(DeviceData, 'DeviceData', self.detected_sensor_callback, 10, callback_group=self.callback_group)
        # 뒤로가기 위한 동작 
        self.cmd_vel_pub = self.create_publisher(Twist, '/base_controller/cmd_vel_unstamped', 10)

        # 만든 변수들 
        self.response_compete = 1
        self.detected_standing = 0
        self.detected_walking = 0
        self.detected_basket = 1
        self.aruco_driving_done = 0
        self.push_button = 0
        self.detected_sensor = 0
        self.driving_status = ""
        self.goto_pose_running = False

        # 이벤트 객체 초기화
        self.driving_status_event = Event()
        self.aruco_driving_event = Event()
        self.pickup_event = Event()

    def yolo_callback(self, msg):
        self.detected_standing = msg.standing
        self.detected_walking = msg.walking
        self.detected_basket = msg.basket

    def detected_sensor_callback(self, msg):
        self.push_button = msg.push_button
        self.detected_sensor = msg.detected_sensor

    def allocatd_job(self, request, response):
        self.get_logger().info(f'Received request: robot_num={request.robot_num}, x={request.x}, y={request.y}, z={request.z}, w={request.w}, job_id={request.job_id}, nav_id={request.nav_id}')
        self.get_logger().info("Job received successfully.")
        response.receive_complete = self.response_compete

        #변수에 request 값 저장
        self.current_request_data = request
        
        threading.Thread(target=self.goto_pose, args=(request,)).start()                  

        return response

    def drivingStatus_server(self, request, response):       
        self.driving_status = request. driving_status    
        self.get_logger().info(f'Received driving_status request: driving_status={request.driving_status}')

        response.receive_complete = self.response_compete

        self.driving_status_event.set() # 이벤트 신호 설정

        return response
    
    def aruco_done(self, request, response):
        self.get_logger().info(f'Received request: pos_calib_complete ={request.pos_calib_complete}')
        self.get_logger().info("Aruco Driving successfully.")
        
        self.aruco_driving_done = request.pos_calib_complete

        response.rec_response = True

        self.aruco_driving_event.set()  # 동작 완료 받았음을 알림
        return response 

    def set_goal_pose(self, goal_pose, nav_id, request_data=None):
     
        if 0 < nav_id <= 9:
            self.get_logger().info(f"nav_id_1 = {nav_id}")
            goal_pose.pose.position.x = request_data.x
            goal_pose.pose.position.y = request_data.y
            goal_pose.pose.orientation.w = request_data.w
            goal_pose.pose.orientation.z = request_data.z
            self.shared_state.robot_status = "driving"
        elif nav_id in (0,10): #0: job 취소 / 10: 작업완료 후 충전소 이동
            #충전소 1 위치
            self.get_logger().info(f"nav_id_2 = {nav_id}")
            self.shared_state.robot_status = "idle"
            goal_pose.pose.position.x = -0.132544
            goal_pose.pose.position.y = 0.090852
            goal_pose.pose.orientation.w = 0.998660
            goal_pose.pose.orientation.z = 0.051749 
        else:
            self.get_logger().error(f"Invalid nav_id: {nav_id}")

    def goto_pose(self, request_data):
        if self.goto_pose_running:
            self.nav.cancelTask()  # 이전 작업 취소
            self.aruco_driving_event.set()
            time.sleep(0.02)

        self.goto_pose_running = True

        self.get_logger().info("Executing post-return action...")

        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = self.nav.get_clock().now().to_msg()

        nav_id =  request_data.nav_id
       
        if nav_id == 0:  # 작업 취소 요청 (충전소로 이동)
            self.get_logger().info("Job cancel requested. Moving to charging station...")
            self.set_goal_pose(goal_pose, nav_id=0, request_data=request_data)
        else:
            self.get_logger().info("Job requested. Moving to destination!!")            
            self.set_goal_pose(goal_pose, nav_id=nav_id, request_data=request_data)
        
        self.nav.goToPose(goal_pose)
        print("===================gotogoal============================")
        self.get_logger().info("Goal pose sent to navigator")
        
        # 주행 상태 초기화
        self.driving_status = ""
        
        self.get_logger().info("driving...")
        # timeout 설정으로 무한 대기 방지
        if not self.driving_status_event.wait(timeout=120.0):  # 60초 타임아웃
            self.get_logger().error("driving timeout")
            self.job_complete_client(job_complete=0, detected_sensor=0)
            self.driving_status_event.clear()
            self.goto_pose_running = False
            return
        
        self.driving_status_event.clear()
        
        # # # 결과 확인
        result = self.driving_status
        # result = "driving success"
        if result == "driving success":      
            print("result ===================================", result)      
            self.get_logger().info("Arrived at destination successfully.")
            # 목적지에 따른 동작 구분
            print("nav_id ===========================", nav_id)
            if 0 < nav_id <= 6: #목적지 6곳
                self.get_logger().info("nav_id <= 6")
                self.check_for_basket()
            elif nav_id in (8, 9):
                self.get_logger().info("nav_id <= 8, 9")
                self.check_for_pushButon()
            elif nav_id == 0:
                self.get_logger().info("nav_id == 0")
                self.shared_state.robot_status = "charging"
        else:
            print("result ===================================", result) 
            self.get_logger().info("Failed to reach the destination.")
            # self.job_complete_client(job_complete=0, detected_sensor=0)
            #성공이 아닐때의 값self.job_complete(request_data, job_complete=0)

        self.goto_pose_running = False

    def move_backwards(self, duration):
        """로봇을 뒤로 이동시키는 함수"""
        cmd = Twist()
        cmd.linear.x = -0.1  # 뒤로 이동 속도
        cmd.angular.z = 0.0

        start_time = self.get_clock().now()

        # 일정 시간 동안 뒤로 이동 명령 발행
        while (self.get_clock().now() - start_time).nanoseconds / 1e9 < duration:
            self.cmd_vel_pub.publish(cmd)
            time.sleep(0.1)  # 100ms 간격으로 발행

        # 정지 명령 발행
        cmd.linear.x = 0.0
        self.cmd_vel_pub.publish(cmd)

        self.get_logger().info(f"Robot moved backwards for {duration} seconds.")
    
    def move_to_charging_station(self):
        self.get_logger().info("Moving to charging station...")
        self.shared_state.robot_status = "idle"

        # 충전소 위치로 이동 설정
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = self.nav.get_clock().now().to_msg()

        # nav_id=10을 이용하여 충전소로 이동
        self.set_goal_pose(goal_pose, nav_id=10)

        # 네비게이터에 목표 전달
        self.nav.goToPose(goal_pose)
        print("===================gotogoal============================")
        self.get_logger().info("Goal pose for charging station sent to navigator")

        # 주행 상태 초기화
        self.driving_status = ""

        self.get_logger().info("Driving to charging station...")
        if not self.driving_status_event.wait(timeout=120.0):  # 300초 타임아웃
            self.get_logger().error("Driving to charging station timeout")
            self.driving_status_event.clear()
            return
        
        self.driving_status_event.clear()

        # 주행 결과 확인
        result = self.driving_status
        if result == "driving success":
            self.get_logger().info("Arrived at charging station.")
            self.shared_state.robot_status = "charging"
            # 주행 상태 초기화
            self.driving_status = ""
        else:
            self.get_logger().info("Failed to reach the charging station.")

    def check_for_pushButon(self): 
        self.shared_state.robot_status = "waiting"

        rate = self.create_rate(10)  # 10Hz
        while self.push_button != 1:
            if not rp.ok():
                return
            self.get_logger().debug('Waiting for button press...')
            rate.sleep()

        self.get_logger().info('Button pressed!')
        self.job_complete_client(job_complete=1, detected_sensor=0)

    def check_for_basket(self):
        if self.detected_basket == 1:
            # 아루코 마커 기반 이동 시도
            self.get_logger().info("aruco dirve Req")
    
            self.aruco_driving(aruco_start=True)           
            
            # timeout 설정으로 무한 대기 방지
            if not self.aruco_driving_event.wait(timeout=120.0):  # 드라이빙 실패
                self.get_logger().error("aruco driving timeout")
                self.job_complete_client(job_complete=0, detected_sensor=0)
                self.aruco_driving_event.clear()
                return
            else:
                self.aruco_driving_event.clear()
            
            if self.aruco_driving_done == 1:  # 아루코 이동 성공
                self.get_logger().info("picking")
                detected_sensor_result = self.basket_pickup(pickup_req=1)

                if not self.pickup_event.wait(timeout=120.0):  # 픽업 실패
                    self.get_logger().error("pickup timeout")
                    self.job_complete_client(job_complete=0, detected_sensor=0)
                    self.pickup_event.clear()
                    return
                else:
                    self.pickup_event.clear()

                    if detected_sensor_result:  # 픽업 성공
                        self.get_logger().info("Pickup complete")
                        print("sensor ===========", self.detected_sensor)
                        self.job_complete_client(job_complete=1, detected_sensor=self.detected_sensor)       

        else:  # 박스가 없는 경우
            self.get_logger().warn("No basket detected")
            self.job_complete_client(job_complete=0, detected_sensor=0)  

    def aruco_driving(self, aruco_start):
        request = BasketInfo.Request()
        # 서버로 보낼 데이터
        request.basket_exist = aruco_start 
        request.nav_id = self.current_request_data.nav_id
        
        self.get_logger().info(f'Request aruco ={request}')

        future = self.Aruco_client.call_async(request)
        future.add_done_callback(self.handle_aruco_response)
        
        return True    
    
    def handle_aruco_response(self, future):
        response = future.result()
        self.get_logger().info(f'Aruco response received: {response.rec_response}')
        
    def basket_pickup(self, pickup_req):
        request = Pickup.Request()
        # 서버로 보낼 데이터
        request.pickup_req = pickup_req 
        self.get_logger().info(f'Request pickup ={request}')

        future = self.Pickup_client.call_async(request)
        future.add_done_callback(self.handle_pickup_response)
        
        return True
    
    def handle_pickup_response(self, future):
        response = future.result()
        self.pickup_response = response  # 응답 저장
        self.pickup_event.set()  # 응답 받았음을 알림

    def job_complete_client(self, job_complete, detected_sensor):
        request = JobCompleteReq.Request()
        # 서버로 보낼 데이터
        request.job_id = self.current_request_data.job_id
        request.job_complete = job_complete # 0: basket 없음, 1: job 완료
        request.detected_sensor = detected_sensor
        
        self.get_logger().info(f'Request jobcomplete ={request}')
        future = self.jobcomplete_client.call_async(request)
        future.add_done_callback(self.handle_job_complete)

    def handle_job_complete(self, future):
        response = future.result()
        self.get_logger().info(f"Response received: {response}")

        # # 작업 완료 후 뒤로 이동 nav_id 보고 뒤로
        print("nav_id =================", self.current_request_data.nav_id)
        if response.receive_complete == 1 and self.current_request_data.nav_id > 0 and self.current_request_data.nav_id < 7:
            self.move_backwards(3)  # 3초 뒤로 이동

        self.shared_state.robot_status = "idle"
        # 충전소로 이동
        self.move_to_charging_station()


def main(args=None):
    rp.init(args=args)

    shared_state = SharedState()

    JobAllocated_srv = JobAllocatedServer(shared_state)
    RobotStatus = RobotStatusPublisher(shared_state)
    
    # MultiThreadedExecutor 사용
    executor = MultiThreadedExecutor()
    executor.add_node(JobAllocated_srv)
    executor.add_node(RobotStatus)
    
    try:
        executor.spin()
    finally:
        executor.shutdown()
        JobAllocated_srv.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()
