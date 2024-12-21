import rclpy as rp
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

import threading
from threading import Event 
import time

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
        
        # # # gui 서버 연결 확인
        # while not self.Aruco_client.wait_for_service(timeout_sec=1.0):
        #     self.get_logger().info('Waiting for JobCompleteReq service...')

        # 만든 변수들 
        self.response_compete = 1
        self.detected_standing = 0
        self.detected_walking = 0
        self.detected_basket = 1
        self.aruco_driving_done = 0
        self.push_button = 0
        self.detected_sensor = 0
        self.driving_status = ""

        self.driving_status_event = Event()
        self.aruco_event = Event()
        self.pickup_event = Event()


    def yolo_callback(self, msg):
        self.detected_standing = msg.standing
        self.detected_walking = msg.walking
        self.detected_basket = msg.basket

    def detected_sensor_callback(self, msg):
        self.push_button = msg.push_button
        self.detected_sensor = msg.detected_sensor

    def allocatd_job(self, request, response):
        self.get_logger().info(f'Received request: robot_num={request.robot_num}, x={request.x}, y={request.y}, theta={request.z}, theta={request.w}, job_id={request.job_id}, nav_id={request.nav_id}')
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

        return response
    
    def aruco_done(self, request, response):
        self.get_logger().info(f'Received request: pos_calib_complete ={request.pos_calib_complete}')
        self.get_logger().info("Aruco Driving successfully.")
        
        self.aruco_driving_done = request.pos_calib_complete

        response.rec_response = True
        
        return response 

    def goto_pose(self, request_data):
        self.get_logger().info("Executing post-return action...")

        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = self.nav.get_clock().now().to_msg()
       
        # 목적지 : nav_id > 0 / 작업 취소 : nav_id = 0
        if 0 < request_data.nav_id <= 9:  ##############################
            self.get_logger().info(f"nav_id_1 = {request_data.nav_id}")          
            goal_pose.pose.position.x = request_data.x
            goal_pose.pose.position.y = request_data.y
            goal_pose.pose.orientation.w = request_data.w
            goal_pose.pose.orientation.z = request_data.z
            self.shared_state.robot_status = "driving"
            self.driving_status_event.set() # 이벤트 신호 설정
        elif request_data.nav_id == 0: 
            self.get_logger().info(f"nav_id_2 = {request_data.nav_id}")   
            self.nav.cancelTask()
            self.shared_state.robot_status = "idle"  
            goal_pose.pose.position.x = -0.186793
            goal_pose.pose.position.y = -0.359778 
            goal_pose.pose.orientation.w = 0.996083
            goal_pose.pose.orientation.z = 0.088418

        nav_id =  request_data.nav_id

       
        self.nav.goToPose(goal_pose)
        self.get_logger().info("Goal pose sent to navigator")
        
        # 주행 상태 초기화
        self.driving_status = ""
        
        self.get_logger().info("driving...")
        # timeout 설정으로 무한 대기 방지
        if not self.driving_status_event.wait(timeout=300.0):  # 60초 타임아웃
            self.get_logger().error("driving timeout")
            self.job_complete_client(job_complete=0, detected_sensor=0)
            return
         
        # # # 결과 확인
        result = self.driving_status
        # result = "driving success"
        if result == "driving success":
            self.get_logger().info("Arrived at destination successfully.")
            # 목적지에 따른 동작 구분
            if nav_id <= 6: #목적지 6곳
                self.check_for_basket()
            elif nav_id in (8, 9):
                self.check_for_pushButon()
        else:
            self.get_logger().info("Failed to reach the destination.")
            #성공이 아닐때의 값self.job_complete(request_data, job_complete=0)

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
            aruco_req_result = self.aruco_driving(aruco_start=True)
           
            # 아루코 이벤트 초기화
            self.aruco_event.clear()
            self.aruco_driving_done = False
                
            if not aruco_req_result:
                self.get_logger().warn("aruco drive Fail")
                self.job_complete_client(job_complete=0, detected_sensor=0)
                return

            self.get_logger().info("aruco driving wait...")
            # timeout 설정으로 무한 대기 방지
            if not self.aruco_event.wait(timeout=60.0):  # 60초 타임아웃
                self.get_logger().error("aruco driving timeout")
                self.job_complete_client(job_complete=0, detected_sensor=0)
                return
            
            if self.aruco_driving_done == 1:  # 아루코 이동 성공
                self.get_logger().info("picking")
                detected_sensor_result = self.basket_pickup(pickup_req=1)
                
                if detected_sensor_result.pickup_response == 1:  # 픽업 성공
                    self.get_logger().info("Pickup complete")
                    self.job_complete_client(job_complete=1, detected_sensor=detected_sensor_result)
                else:  # 픽업 실패
                    self.get_logger().warn("Pickup failed")
                    self.job_complete_client(job_complete=0, detected_sensor=0)
            
            else:  # 아루코 이동 실패
                self.get_logger().warn("Aruco driving failed")
                self.job_complete_client(job_complete=0, detected_sensor=0)
        
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
        self.aruco_event.set()  # 응답 받았음을 알림

    def basket_pickup(self, pickup_req):
        request = Pickup.Request()
        # 서버로 보낼 데이터
        request.pickup_req = pickup_req 
        self.get_logger().info(f'Request pickup ={request}')
        future = self.Pickup_client.call_async(request)
        rp.spin_until_future_complete(self, future)

        # 서버에서 받을 데이터
        response = future.result()
     
        return response

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
        self.shared_state.robot_status = "idle"


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
