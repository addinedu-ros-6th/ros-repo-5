import rclpy as rp
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

import threading
import time

from taskmanager_msgs.srv import JobAllocated, JobCompleteReq
from minibot_interfaces.srv import Pickup
from camera_interface.msg import YoloDetect
from taskmanager_msgs.msg import RobotStatus
from minibot_interfaces.msg import DeviceData
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult


class RobotStatusPublisher(Node):
	
	def __init__(self):
		super().__init__('RobotStatus_Publisher')
		self.publisher = self.create_publisher(RobotStatus, 'RobotStatus', 10)
		self.subscription = self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose',self.pose_callback, 10)
		self.subscription

		timer_period = 0.5
		self.timer = self.create_timer(timer_period, self.status_callback)
		
		self.robot_status = ""
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
			self.battery_status -= 1
			msg.battery_status = self.battery_status
			self.battery_time = 0
		else: 
			msg.battery_status = self.battery_status

		msg.robot_status = "idle"
		msg.x = self.robot_pose_x
		msg.y = self.robot_pose_y

		self.publisher.publish(msg)

class JobAllocatedServer(Node):

    def __init__(self):
        super().__init__('JobAllocated_server')
        self.callback_group = ReentrantCallbackGroup()
        self.nav = BasicNavigator()

        self.joballocate_server = self.create_service(JobAllocated, 'JobAllocatedRes', self.allocatd_job, callback_group=self.callback_group)
        self.jobcomplete_client = self.create_client(JobCompleteReq, 'JobCompleteReq', callback_group=self.callback_group)
        self.yolo_subscription = self.create_subscription(YoloDetect, 'yolo_detect', self.yolo_callback, 10, callback_group=self.callback_group)
        self.yolo_subscription
        self.detected_sensor_subscription = self.create_subscription(DeviceData, 'DeviceData', self.detected_sensor_callback, 10, callback_group=self.callback_group)
        self.detected_sensor_subscription
        self.PickupServer = self.create_client(Pickup, 'PickupServer', callback_group=self.callback_group)

        # # 서버 연결 확인
        while not self.jobcomplete_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for JobCompleteReq service...')

        # 만든 변수들 
        self.response_compete = 1
        self.detected_standing = 0
        self.detected_walking = 0
        self.detected_basket = 1

    def yolo_callback(self, msg):
        self.detected_standing = msg.standing
        self.detected_walking = msg.walking
        self.detected_basket = msg.basket

    def detected_sensor_callback(self, msg):
        self.push_button = msg.push_button
        self.detected_sensor = msg.detected_sensor

    def allocatd_job(self, request, response):
        self.get_logger().info(f'Received request: robot_num={request.robot_num}, x={request.x}, y={request.y}, theta={request.z}, theta={request.w}, job_id={request.job_id}')
        self.get_logger().info("Job received successfully.")
        response.receive_complete = self.response_compete

        #변수에 request 값 저장
        self.current_request_data = request
        
        # 정상 적으로 값이 들어왔을 때 이동 시작
        if request.x != 0.0 and request.y != 0.0 and request.w != 0 and request.z != 0:
            # `goto_pose` 작업을 별도 스레드에서 실행
            threading.Thread(target=self.goto_pose, args=(request,)).start()
        else:
            self.nav.cancelTask()

        return response

    def goto_pose(self, request_data):
        self.get_logger().info("Executing post-return action...")

        # 이동 목표 설정
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = self.nav.get_clock().now().to_msg()
        goal_pose.pose.position.x = request_data.x
        goal_pose.pose.position.y = request_data.y
        goal_pose.pose.orientation.w = request_data.w
        goal_pose.pose.orientation.z = request_data.z
        
        self.nav.goToPose(goal_pose)
        self.get_logger().info("Goal pose sent to navigator")
        
        # 이동 완료 여부 확인
        while not self.nav.isTaskComplete():
            time.sleep(0.1)  # 0.5초마다 이동 완료 여부를 확인

        # 결과 확인
        result = self.nav.getResult()
        if result == TaskResult.SUCCEEDED:
            self.get_logger().info("Arrived at destination successfully.")
            self.check_for_basket()
        else:
            self.get_logger().info("Failed to reach the destination.")
            #성공이 아닐때의 값self.job_complete(request_data, job_complete=0)

    def check_for_basket(self):
        #박스가 있으면 test = 1, 0
        test = 1
        # if self.detected_basket == 1:
        if test == 1:
            # detected_sensor_result = self.basket_pickup(pickup_req = 1)
            # self.job_complete_client(job_complete=1, detected_sensor=detected_sensor_result)
            self.job_complete_client(job_complete=1, detected_sensor=1)
        else: #박스가 없으면
            self.job_complete_client(job_complete=0, detected_sensor=0)

    def basket_pickup(self, pickup_req):
        #동작 신호 보내고 응답 확인
        request = Pickup.Request()
        # 서버로 보낼 데이터
        request.pickup_req = pickup_req 

        future = self.PickupServer.call_async(request)
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

        future = self.jobcomplete_client.call_async(request)
        print("==========", job_complete,detected_sensor)
        future.add_done_callback(self.handle_job_complete)

    def handle_job_complete(self, future):
        response = future.result()
        self.get_logger().info(f"Response received: {response}")

def main(args=None):
    rp.init(args=args)

    JobAllocated_srv = JobAllocatedServer()
    RobotStatus = RobotStatusPublisher()
    
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
