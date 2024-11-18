import rclpy as rp
from rclpy.node import Node
import RPi.GPIO as GPIO
from minibot_interfaces.msg import DeviceData
from minibot_interfaces.srv import Pickup
import time

class TrashBotDevice(Node):
    def __init__(self):
        super().__init__('led_blinker_node')
        self.DeviceData_publisher = self.create_publisher(DeviceData, 'DeviceData', 10)
        self.PickupServer = self.create_service(Pickup, 'PickupServer', self.callback_service)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # GPIO 설정
        GPIO.setwarnings(False)
    
        GPIO.setmode(GPIO.BOARD) # 피 번호로 입력
        self.Button_PIN = 11  # 제어할 GPIO 핀 번호
        GPIO.setup(self.Button_PIN, GPIO.IN)
        self.DetectedSensor_PIN = 13  # 제어할 GPIO 핀 번호
        GPIO.setup(self.DetectedSensor_PIN, GPIO.IN)   

        self.servo_pin1 = 33
        self.servo_pin2 = 32
        GPIO.setup(self.servo_pin1, GPIO.OUT)  
        GPIO.setup(self.servo_pin2, GPIO.OUT)
        
        self.servo1 = GPIO.PWM(self.servo_pin1, 50)
        self.servo2 = GPIO.PWM(self.servo_pin2, 50)
       

        time.sleep(1)
        self.servo1.start(2.5)
        self.servo2.start(2.5)

    def timer_callback(self): #버튼이 눌렸을때만 publish
        msg = DeviceData()	
        button_state = GPIO.input(self.Button_PIN)
        detectedSensor_state = GPIO.input(self.DetectedSensor_PIN)
        
        if button_state == 1:
            msg.push_button = 1
        else:
            msg.push_button = 0
        
        if detectedSensor_state == 1:
            msg.detected_sensor = 1
        else:
            msg.detected_sensor = 0

        self.DeviceData_publisher.publish(msg)

    def callback_service(self, request, response):
        print('requeset : ', request.pickup_req)
        if request.pickup_req == 1:
            print('picker start')
            self.perform_picker_action()
            response.pickup_done = 1
        else:
            response.pickup_done = 0

        return response  
        
    def perform_picker_action(self):
        # Servo2를 10도에서 110도로 회전
        for angle in range(10, 90): 
            duty_cycle = self.angle_to_duty_cycle(angle)
            self.servo2.ChangeDutyCycle(duty_cycle)
            time.sleep(0.02)
        time.sleep(2)

        # Servo1을 0도에서 90도로 회전
        for angle in range(0, 80):  
            duty_cycle = self.angle_to_duty_cycle(angle)
            self.servo1.ChangeDutyCycle(duty_cycle)
            time.sleep(0.02)
        time.sleep(2)

        # Servo1을 다시 90도에서 0도로 회전
        for angle in range(80, -1, -1): 
            duty_cycle = self.angle_to_duty_cycle(angle)
            self.servo1.ChangeDutyCycle(duty_cycle)
            time.sleep(0.02)
        time.sleep(1)

        # Servo2를 110도에서 10도로 회전
        for angle in range(90, 9, -1):  
            duty_cycle = self.angle_to_duty_cycle(angle)
            self.servo2.ChangeDutyCycle(duty_cycle)
            time.sleep(0.02)

        print("Picker action complete.")
    
    # 각도를 듀티 사이클로 변환하는 함수
    def angle_to_duty_cycle(self, angle):
        # 0도 -> 2.5%, 90도 -> 7.5%, 180도 -> 12.5%
        return (angle / 18.0) + 2.5


def main(args=None):
    rp.init(args=args)
    
    Trashbot = TrashBotDevice()
    rp.spin(Trashbot)
    Trashbot.destroy_node()
    rp.shutdown()
    GPIO.cleanup()


if __name__ == '__main__':
    main()