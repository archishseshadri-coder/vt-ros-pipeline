import rclpy
from rclpy.node import Node
from std_msgs.msg import String # Changed to String to hold data + time
import random
import time

class MockPiNode(Node):
    def __init__(self):
        super().__init__('mock_pi_node')
        self.publisher_ = self.create_publisher(String, 'eeg_classification', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        command = random.randint(0, 3)
        timestamp = time.time() # Current time in seconds
        
        # Package data as "Command|Timestamp"
        msg.data = f"{command}|{timestamp}"
        
        self.publisher_.publish(msg)
        self.get_logger().info(f'Sent: {command} at {timestamp}')

def main(args=None):
    rclpy.init(args=args)
    node = MockPiNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
