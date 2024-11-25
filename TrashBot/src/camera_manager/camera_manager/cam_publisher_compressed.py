import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
import cv2

class CameraPublisherCompressed(Node):
    def __init__(self):
        super().__init__('camera_publisher_compressed')
        
        # 압축된 이미지를 발행할 토픽 생성
        self.publisher_ = self.create_publisher(CompressedImage, 'image_raw/compressed', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        # Pi Camera 설정
        self.cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            # 이미지를 JPEG로 압축하여 메시지에 저장
            frame_resized = cv2.resize(frame, (640,480))
            
            success, encoded_image = cv2.imencode('.jpg', frame_resized)
            if success:
                image_message = CompressedImage()
                image_message.format = "jpeg"
                image_message.data = encoded_image.tobytes()
                self.publisher_.publish(image_message)
                self.get_logger().info('Publishing compressed image frame')

    def destroy_node(self):
        self.cap.release()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    camera_publisher_compressed = CameraPublisherCompressed()
    rclpy.spin(camera_publisher_compressed)
    camera_publisher_compressed.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
