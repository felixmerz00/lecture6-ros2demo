import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdomMonitor(Node):
    def __init__(self):
        super().__init__("odom_subscriber")
        self.subscription = self.create_subscription(Odometry, "/odom", self.odom_callback, 1)
        self.get_logger().info("Listening to odometry")
    
    def odom_callback(self, msg):
        pos = msg.pose.pose.position
        self.get_logger().info(
            f'Robot at x={pos.x:.2f}, y={pos.y:.2f}'
        )

def main(args=None):
    rclpy.init(args=args)
    monitor_node = OdomMonitor()
    rclpy.spin(monitor_node)

    monitor_node.destroy_node()
    rclpy.shutdown()
