import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
import numpy as np
import cv2
from deeplearning_manager import ArucoDetector
from ultralytics import YOLO

mtx = np.array([     [525.566650732664,	0,	305.54479000255], 
                     [0,	527.23218285717,	252.170579252493 ], 
                     [0., 0., 1. ]])    

dist = np.array([[0.211189793800737,	-0.0217810236473847,	0.0223407502790141,	-0.0171287737674997,	-1.41551261978435]])

class ImageSubscriberCompressed(Node):
    def __init__(self, camera_matrix, dist_coeffs):
        super().__init__('image_subscriber_compressed')
        
        # 압축된 이미지를 구독할 토픽 생성
        self.subscription = self.create_subscription(
            CompressedImage,
            'image_raw/compressed',
            self.listener_callback,
            10)
        
        # ArUcoDetector 인스턴스 생성
        self.aruco_detector = ArucoDetector(camera_matrix, dist_coeffs)

        self.yolo_model = YOLO("/home/sh/dev_ws/PJT/ROS/model/best_1101.pt")

    def listener_callback(self, msg):
        # 수신한 데이터를 디코딩하여 이미지로 변환
        np_arr = np.frombuffer(msg.data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        
        # ArUco 마커를 탐지하고 주석을 추가
        annotated_frame, detected_markers = self.aruco_detector.detect_and_annotate(frame)

        # YOLOv8을 사용한 장애물 탐지
        results = self.yolo_model(annotated_frame) 

        annotated_frame = results[0].plot()
        
        # for result in results:
        #     boxes = result.boxes  # 감지된 바운딩 박스
        #     for box in boxes:
        #         x1, y1, x2, y2, conf, cls = box.xyxy[0].numpy()  # 바운딩 박스 좌표와 확률, 클래스
        #         label = f"{self.yolo_model.names[int(cls)]} {conf:.2f}"  # 클래스 레이블

        #         # 바운딩 박스 그리기
        #         cv2.rectangle(annotated_frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
        #         cv2.putText(annotated_frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # 감지된 마커 ID, 2D 좌표, 3D 위치 좌표 출력
        for marker in detected_markers:
            self.get_logger().info(f"Detected ArUco Marker - ID: {marker['id']}, "
                                   f"2D Center: {marker['center_2d']}, "
                                   f"3D Position: {marker['position_3d']}, "
                                   f"Distance: {marker['distance']}")

        # 결과를 표시
        cv2.imshow("Picam", annotated_frame)
        cv2.waitKey(1)

def main(args=None):
    # 예시 카메라 매트릭스와 왜곡 계수 (카메라 캘리브레이션을 통해 얻은 값으로 대체 필요)
    
    rclpy.init(args=args)
    image_subscriber_compressed = ImageSubscriberCompressed(mtx, dist)
    rclpy.spin(image_subscriber_compressed)
    image_subscriber_compressed.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()