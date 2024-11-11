import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from camera_interface.msg import YoloDetect
import numpy as np
import cv2
from ultralytics import YOLO

class ImageSubscriberCompressed(Node):
    def __init__(self):
        super().__init__('image_subscriber_yolo')
        
        # 압축된 이미지를 구독할 토픽 생성
        self.subscription = self.create_subscription(CompressedImage, 'image_raw/compressed', self.detect_callback, 10)
        self.yoloPublisher = self.create_publisher(YoloDetect, 'yolo_detect', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.publishers_callback)
        self.standing = 0
        self.walking = 0
        self.basket = 0

        self.yolo_model = YOLO("/home/sh/dev_ws/PJT/ROS/model/best_1101.pt")

    def detect_callback(self, msg):
        # 수신한 데이터를 디코딩하여 이미지로 변환
        np_arr = np.frombuffer(msg.data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # YOLOv8을 사용한 장애물 탐지
        results = self.yolo_model(frame) 

        frame = results[0].plot()
        
        for result in results:
            boxes = result.boxes  # 감지된 바운딩 박스
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()  # 바운딩 박스 좌표
                conf = box.conf[0].cpu().numpy()  # 신뢰도
                cls = box.cls[0].cpu().numpy()  # 클래스 ID

                width = x2 - x1
                height = y2 - y1
                area = width * height

                if cls == 0 and area > 30000 and conf > 0.7:
                    self.basket = 1
                elif cls == 1 and area > 9000 and conf > 0.7:
                    self.standing = 1
                elif cls == 2 and area > 10000 and conf > 0.7:
                    self.walking = 1
                else:
                    self.standing = 0
                    self.walking = 0
                    self.basket = 0

                print("area===================", area)

        # 결과를 표시
        cv2.imshow("Picam", frame)
        cv2.waitKey(1)

    def publishers_callback(self): 
        msg = YoloDetect()	
        msg.standing = self.standing		
        msg.walking = self.walking
        msg.basket = self.basket			
        
        self.yoloPublisher.publish(msg)        

def main(args=None):
    rclpy.init(args=args)
    image_subscriber_compressed = ImageSubscriberCompressed()
    rclpy.spin(image_subscriber_compressed)
    image_subscriber_compressed.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()