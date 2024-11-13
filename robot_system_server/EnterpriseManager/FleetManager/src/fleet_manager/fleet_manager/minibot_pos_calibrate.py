import rclpy
from rclpy.node import Node
from camera_interface.srv import ArucoInfo
from camera_interface.srv import BasketInfo
from camera_interface.srv import PosCalibration
import threading
from time import sleep
import math 
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist
# from collections import namedtuple

# Constants = namedtuple('Constants', ['STATE_CALIBRATE', 'STATE_POS_CHECK'])
# constants = Constants(STATE_CALIBRATE=1, STATE_POS_CHECK=2)


class MinibotPosCalibrator(Node):
    def __init__(self):
        super().__init__('minibot_pos_calibrator')
        self.aruco_client = self.create_client(ArucoInfo, '/aruco_marker/pose')
        #self.basket_service = self.create_service(BasketInfo, 'basket_data', self.receive_basket_data)
        #self.pos_calib_client = self.create_client( PosCalibration , 'poscal_data')
        self.bot_vel_pub = self.create_publisher(Twist, '/base_controller/cmd_vel_unstamped', 10)
        
        while not self.aruco_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Aruco Service Waiting...')
        
        self.get_logger().info('Aruco Client Started!!')

        # while not self.pos_calib_client.wait_for_service(timeout_sec=1.0):
        #     self.get_logger().info('pos_calib Service Waiting...')
        
        # self.get_logger().info('pos_calib Client Started!!')
        
        self.aruco_info = {}
        self.skip_aruco_req = False
        self.aruco_req_cnt = 0

        self.complete_action = False

        self.basket_is_exist = True

        self.aurco_event = threading.Event()
        self.cpl_event = threading.Event()

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

    # def cpl_calib_request(self):
    #     request = PosCalibration.Request()
    #     request.pos_calib_completes = True
    #     self.calib_future = self.pos_calib_client.call_async(request)

    #     self.calib_future.add_done_callback(self.handle_calib_response)

    def receive_basket_data(self, request, response):
        response.rec_response = True

        if request.basket_exist: 
            self.basket_is_exist = True 
        else:
            self.basket_is_exist = False
        return response 

    def handle_aruco_response(self, future):
        try:
            response = future.result()
            if response and response.ids:
                self.aruco_req_cnt +=1
                for idx, marker_id in enumerate(response.ids):
                    if 11 == marker_id:
                        self.aruco_info['Position'] = response.positions[idx]
                        self.aruco_info['Distance'] = response.distance[idx]
                        self.get_logger().info(f"Aruco ID: {marker_id}, Position: (x: {self.aruco_info['Position'].x}, y: {self.aruco_info['Position'].y}, z: {self.aruco_info['Position'].z}), Distance: {self.aruco_info['Distance']}")
                        self.skip_aruco_req = True
                        self.aurco_event.set()            
            else:
                self.get_logger().info("Detected Aruco Marker not Exist")
        except Exception as e:
            self.get_logger().error(f"Service call Failed: {e}")
    
    def handle_calib_response(self, future):
        try:            
            response = future.result()
            self.complete_action = response.rec_response
            self.cpl_event.set()
        except Exception as e:
            self.get_logger().error(f"Service call Failed: {e}")            

    def minibot_rotate(self, target_angle, angular_speed):
        twist = Twist()
        twist.angular.z = angular_speed if target_angle > 0 else -angular_speed
        self.get_logger().info(f'twist.angular.z: {twist.angular.z}')
        current_angle = 0.0
        rate = 25  # 초당 10회
        duration = 1 / rate  # 반복 주기

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
            if self.basket_is_exist:
                if not self.skip_aruco_req:
                    self.aruco_info_request()
                    if not self.aurco_event.wait(timeout=1.0):
                        self.get_logger().info('Aruco Event timeout - Retrying')
                    self.aurco_event.clear()
                else:
                    pass

                if len(self.aruco_info) > 0:         
                    pos_x = round( self.aruco_info['Position'].x, 3 )
                    pos_z = round( self.aruco_info['Position'].z, 3 )
                    xz_dis = math.sqrt( math.pow( pos_x , 2 ) + math.pow( pos_z , 2 ) )                        
                    xz_dis = round(xz_dis, 3)       
                    
                    rot_rad = math.atan2(abs(pos_x), abs(pos_z))
                    rot_rad = round( rot_rad , 3)

                    rot_deg = math.degrees(rot_rad)        
                    rot_deg = round( rot_deg , 3)

                    if self.aruco_info['Position'].x > 0:
                        rot_rad = -rot_rad
                        angle_speed = 0.2
                    else:
                        rot_rad = rot_rad
                        angle_speed = 0.15            

                    if xz_dis > 0.16:
                        mov_dis = 0.05          
                        self.get_logger().info(f"xz_dis : {xz_dis}, move_dis : {mov_dis}, rot_rad : {rot_rad}, rot_deg : {rot_deg}")                                  
                        self.minibot_straight(mov_dis)           
                        sleep(1)
                        self.minibot_rotate(rot_rad, angle_speed)                                       
                        self.skip_aruco_req = False
                    else:
                        mov_dis = 0.045
                        self.get_logger().info(f"move_dis : {mov_dis}")                                  
                        self.minibot_straight(mov_dis) 
                        sleep(1)
                        self.minibot_rotate(rot_rad, angle_speed)
                        #self.basket_is_exist = False
                        #self.cpl_calib_request()
                        # if not self.cpl_event.wait(timeout=3.0):
                        #     self.get_logger().info('Not Received Response from FleetManager')                  
                                            
                    self.aruco_info.clear()
                    self.aurco_event.clear()
            else:
                self.get_logger().info('Basket Info Not Received!!')

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