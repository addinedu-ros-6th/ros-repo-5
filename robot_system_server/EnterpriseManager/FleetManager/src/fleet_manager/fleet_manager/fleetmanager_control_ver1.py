import rclpy as rp
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import threading
import time

from taskmanager_msgs.srv import JobAllocated
from taskmanager_msgs.srv import JobCompleteReq


class JobAllocatedServer(Node):

    def __init__(self):
        super().__init__('JobAllocated_server')
        self.callback_group = ReentrantCallbackGroup()
        self.nav = BasicNavigator()

        self.server = self.create_service(JobAllocated, 'JobAllocatedRes', self.allocatd_job, callback_group=self.callback_group)
        self.client = self.create_client(JobCompleteReq, 'JobCompleteReq', callback_group=self.callback_group)

        # 서버 연결 확인
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for JobCompleteReq service...')

        # response_check
        self.response_compete = 1

    def allocatd_job(self, request, response):
        self.get_logger().info(f'Received request: robot_num={request.robot_num}, x={request.x}, y={request.y}, theta={request.z}, theta={request.w}, job_id={request.job_id}')
        self.get_logger().info("Job received successfully.")
        response.receive_complete = self.response_compete
        
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
            self.job_complete(request_data, job_complete=1)
        else:
            self.get_logger().info("Failed to reach the destination.")
            self.job_complete(request_data, job_complete=0)


    def job_complete(self, request_data, job_complete):
        request = JobCompleteReq.Request()
        # 서버로 보낼 데이터
        request.job_id = request_data.job_id
        request.job_complete = job_complete

        future = self.client.call_async(request)
        future.add_done_callback(self.handle_job_complete)

    def handle_job_complete(self, future):
        response = future.result()
        self.get_logger().info(f"Response received: {response}")


def main(args=None):
    rp.init(args=args)

    JobAllocated_srv = JobAllocatedServer()
    
    # MultiThreadedExecutor 사용
    executor = MultiThreadedExecutor()
    executor.add_node(JobAllocated_srv)
    
    try:
        executor.spin()
    finally:
        executor.shutdown()
        JobAllocated_srv.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()
