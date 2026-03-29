import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

class TurtleControl(Node):
    def __init__(self):
        super().__init__('turtle_control_node')
        self.subscription = self.create_subscription(Int32, 'eeg_classification', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def listener_callback(self, msg):
        move_cmd = Twist()
        if msg.data == 1:
            move_cmd.linear.x = 2.0
            move_cmd.angular.z = 0.0
            self.get_logger().info('GO: Moving Forward')
        else:
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 1.5
            self.get_logger().info('STOP: Spinning!')
        self.publisher_.publish(move_cmd)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControl()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
