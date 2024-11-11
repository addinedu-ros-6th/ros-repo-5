import rclpy
from rclpy.node import Node
from camera_interface.srv import ArucoInfo
from camera_interface.srv import BasketInfo
import threading
from time import sleep
import math 
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist
from collections import namedtuple

Constants = namedtuple('Constants', ['STATE_CALIBRATE', 'STATE_CHECK'])
constants = Constants(STATE_CALIBRATE=1, STATE_CHECK=2)


class MinibotPosCalibrator(Node):
    def __init__(self):
        super().__init__('minibot_pos_calibrator')
        self.aruco_client = self.create_client(ArucoInfo, '/aruco_marker/pose')
        self.basket_client = self.create_client(BasketInfo, '/dl_model/basket')

        self.bot_vel_pub = self.create_publisher(Twist, '/base_controller/cmd_vel_unstamped', 10)
        
        while not self.aruco_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Aruco Service Waiting...')
        
        self.get_logger().info('Aruco Client Started!!')

        while not self.aruco_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Basket Service Waiting...')
        
        self.get_logger().info('Basket Client Started!!')

        self.driving_is_success = True
        
        self.basket_is_exist = True
        self.skip_basket_req = False
        self.basket_req_cnt = 0
        
        self.aruco_info = {}
        self.skip_aruco_req = False
        self.aruco_req_cnt = 0

        self.set_bot_state = constants.STATE_CALIBRATE

        self.aurco_event = threading.Event()
        self.basket_event = threading.Event()


        # 위치 보정 쓰레드 시작
        self.cal_thread = threading.Thread(target=self.calibrator_thread)
        self.cal_thread.start()
        
        self.get_logger().info("Minibot Pos Calibrator Started !!")

    def aruco_info_request(self):
        request = ArucoInfo.Request()
        request.aruco_info_req = True
        self.aruco_future = self.aruco_client.call_async(request)
        
        # 완료된 후 결과를 처리할 콜백 함수 등록
        self.aruco_future.add_done_callback(self.handle_aruco_response)

    def basket_info_request(self):
        request = BasketInfo.Request()
        request.basket_info_req = True
        self.basket_future = self.basket_client.call_async(request)

        # 완료된 후 결과를 처리할 콜백 함수 등록
        self.basket_future.add_done_callback(self.handle_basket_response)

    def handle_aruco_response(self, future):
        try:
            response = future.result()
            if response and response.ids:
                self.aruco_req_cnt +=1
                for idx, marker_id in enumerate(response.ids):
                    if 44 == marker_id:
                        self.aruco_info['Position'] = response.positions[idx]
                        self.aruco_info['Distance'] = response.distance[idx]
                        self.get_logger().info(f"Aruco ID: {marker_id}, Position: (x: {self.aruco_info['Position'].x}, y: {self.aruco_info['Position'].y}, z: {self.aruco_info['Position'].z}), Distance: {self.aruco_info['Distance']}")
                        self.skip_aruco_req = True
                        self.aurco_event.set()            
            else:
                self.get_logger().info("Detected Aruco Marker not Exist")
        except Exception as e:
            self.get_logger().error(f"Service call Failed: {e}")

    def handle_basket_response(self, future):
        try:
            response = future.result()
            #self.basket_req_cnt+=1
            if response:
                self.basket_event.set()
                self.basket_is_exist = response.basket_exist
                if self.basket_is_exist == True:
                    self.skip_basket_req = True
            else:
                self.get_logger().info('Response is None!')     
        except Exception as e:
            self.get_logger().error(f'Service call Failed: {e}')

    def minibot_rotate(self, target_angle, angular_speed = 0.04):
        twist = Twist()
        twist.angular.z = angular_speed

        current_angle = 0.0
        rate = 20
        duration = 1 / rate 

        self.get_logger().info('Enter Rotate Routine')
        while abs(current_angle) < abs(target_angle):
            self.bot_vel_pub.publish(twist)
            sleep(duration)
            current_angle += angular_speed * duration

        twist.angular.z = 0.0
        self.bot_vel_pub.publish(twist)

    def minibot_straight(self, target_distance, linear_speed = 0.03):
        twist = Twist()
        twist.linear.x = linear_speed 
        current_distance = 0.0
        rate = 25
        duration = 1 / rate 

        self.get_logger().info('Enter straight Routine')
        while abs(current_distance) < abs(target_distance):
            self.bot_vel_pub.publish(twist)
            sleep(duration)
            current_distance += linear_speed * duration

        twist.linear.x = 0.0 
        self.bot_vel_pub.publish(twist)

        
    def calibrator_thread(self):
        while rclpy.ok():          
            if self.driving_is_success:
                #if not self.skip_basket_req: 
                #    self.basket_info_request()

                if not self.skip_aruco_req:
                    self.aruco_info_request()
                    if not self.aurco_event.wait(timeout=1.0):
                        self.get_logger().info('Aruco Event timeout - Retrying')
                    self.aurco_event.clear()

                if self.basket_is_exist:
                    if len(self.aruco_info) > 0:         
                        pos_x = round( self.aruco_info['Position'].x, 3 )
                        pos_z = round( self.aruco_info['Position'].z, 3 )
                        xz_dis = math.sqrt( math.pow( pos_x , 2 ) + math.pow( pos_z , 2 ) )                        
                        xz_dis = round(xz_dis, 3)          

                        if self.set_bot_state == constants.STATE_CALIBRATE:         
                            rot_rad = math.atan2(abs(pos_x), abs(pos_z))
                            rot_deg = math.degrees(rot_rad)

                            mov_dis = ( xz_dis + 0.02 )
                            
                            if self.aruco_info['Position'].x > 0:
                                rot_rad = -rot_rad
                            else:
                                rot_rad = rot_rad

                            self.get_logger().info(f"move_dis : {mov_dis}, rot_rad : {rot_rad}, rot_deg : {rot_deg}")

                            self.minibot_rotate(rot_rad)
                            sleep(1.5)
                            self.minibot_straight(mov_dis)
                            
                        #     bf_xz_dis = xz_dis
                        #     self.skip_aruco_req = False
                        #     self.set_bot_state = constants.STATE_CHECK
                        # else: #self.set_bot_state == constants.STATE_CHECK
                        #     af_xz_dis = xz_dis 
                        #     err_dis = bf_xz_dis - af_xz_dis 

                        #     if err_dis - mov_dis < 0.012: 
                        #         self.driving_is_success = False
                        #         self.basket_is_exist = False
                        #         self.skip_basket_req = False 
                        #         self.skip_aruco_req = False
                        #         self.basket_req_cnt = 0                                
                        #     else:
                        #         self.set_bot_state = constants.STATE_CALIBRATE
                            
                        # self.aruco_req_cnt = 0
                        self.aruco_info.clear()
                        self.aurco_event.clear()
                    else:
                        if self.aruco_req_cnt > 5:
                            self.get_logger().info('Aruco Check Count over assigned count!!')
                            
                else:
                    #Basket Image 찍어서 Server 전송 서비스 인터페이스로 Deeplearning Manager와 통신
                    if self.basket_req_cnt > 5:
                        self.get_logger().info('Basket Check Count over assigned count!!') 
            else:
                self.get_logger().info('Driving in progress')

def main(args=None):
    rclpy.init(args=args)

    minibot_calc_node = MinibotPosCalibrator()

    try:
        rclpy.spin(minibot_calc_node)
    except KeyboardInterrupt:
        pass
    finally:
        minibot_calc_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()