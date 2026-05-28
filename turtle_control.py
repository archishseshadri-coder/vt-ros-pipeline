import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import time


# SYSTEM SETTINGS (Flexible Interface)
TOPIC_NAME = 'eeg_classification'
LINEAR_SPEED = 2.0   # Adjust for faster/slower forward movement
ANGULAR_SPEED = 1.5  # Adjust for sharper/wider turns


class TurtleControl(Node):
    def __init__(self):
        super().__init__('turtle_control_node')
        # Using the flexible TOPIC_NAME variable
        self.subscription = self.create_subscription(String, TOPIC_NAME, self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def listener_callback(self, msg):
        # Unpack message and timestamp
        try:
            data_parts = msg.data.split('|')
            command = int(data_parts[0])
            sent_time = float(data_parts[1])
            
            # Latency math
            latency = (time.time() - sent_time) * 1000
            
            move_cmd = Twist()
            
            # Logic using flexible speed variables
            if command == 1: 
                move_cmd.linear.x = LINEAR_SPEED
            elif command == 2: 
                move_cmd.angular.z = ANGULAR_SPEED
            elif command == 3: 
                move_cmd.angular.z = -ANGULAR_SPEED
            
            self.publisher_.publish(move_cmd)
            self.get_logger().info(f'LATENCY: {latency:.2f}ms | CMD: {command}')
            
        except Exception as e:
            self.get_logger().error(f'Failed to parse message: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControl()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
