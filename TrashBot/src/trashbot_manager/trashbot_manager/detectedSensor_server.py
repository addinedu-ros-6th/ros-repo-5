from minibot_interfaces.srv import SensorData

import rclpy as rp
from rclpy.node import Node

class sensordatasever(Node):

    def __init__(self):
        super().__init__('sensordata')
        self.server = self.create_service(SensorData, 'detectedSensordata', self.callback_service)
       
    def callback_service(self, request, response):
        print('requeset : ', request.num)
        if request.num == 1:
            response.detectedsensor_1 = 0
            response.detectedsensor_2 = 1
            print('picker start')
        else:
            print('not process')
        return response  
    
def main(args=None):
    rp.init(args=args)
    sensordata_srv = sensordatasever()
    rp.spin(sensordata_srv)
    rp.shutdown()

if __name__ == '__main__':
    main()