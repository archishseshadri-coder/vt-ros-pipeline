import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class MockPi(Node):
    def __init__(self):
        super().__init__('mock_pi_node')
        # This creates the "Topic" (radio station)
        self.publisher_ = self.create_publisher(Int32, 'eeg_classification', 10)
        self.timer = self.create_timer(2.0, self.timer_callback) 

    def timer_callback(self):
        msg = Int32()
        msg.data = random.choice([0, 1]) 
        self.publisher_.publish(msg)
        self.get_logger().info(f'Mock Pi sending signal: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = MockPi()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
