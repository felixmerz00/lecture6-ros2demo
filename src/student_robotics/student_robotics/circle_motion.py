import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TwistPublisher(Node):
    def __init__(self):
        super().__init__('twist_publisher')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
    
    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.3  # m/s forward
        msg.angular.z = 0.5     # rad/s turn
        self.publisher.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)
    my_node = TwistPublisher()
    rclpy.spin(my_node)

    my_node.destroy_node()
    rclpy.shutdown()