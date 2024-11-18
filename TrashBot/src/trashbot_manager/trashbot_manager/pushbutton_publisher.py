import rclpy as rp
from rclpy.node import Node

from minibot_interfaces.msg import PushButton

class PushButtonPublisher(Node):
	
    def __init__(self):
        super().__init__('pushbutton_pub')
        self.publisher = self.create_publisher(PushButton, 'pushbutton', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.x = 0

    def timer_callback(self): #버튼이 눌렸을때만 publish
        msg = PushButton()	
        msg.button = self.x			
        self.x += 1	
        if self.x > 10:
            self.publisher.publish(msg)
            self.x = 0
    
def main(args=None):
    rp.init(args=args)

    pushbutton_publisher = PushButtonPublisher()
    rp.spin(pushbutton_publisher)

    pushbutton_publisher.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()