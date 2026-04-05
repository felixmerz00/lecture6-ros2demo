# Exercise 6: ROS 2 Concepts & Building Software Packages

[My fork](https://github.com/felixmerz00/lecture6-ros2demo), Felix Merz, student ID, ROS2 Humble


## Exercise 1
### a)
![screenshot folder structure](images/1a-tree-of-package.png)
```Python
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
```
![screenshot of a simulated TurtleBot3 in Gazebo](images/1a-robot-moving-in-circles.png)

`create_timer()` is an inherited method from the `Node` class that creates a timer that calls the provided callback method in the provided interval, i.e. it calls the `self.timer_callback` ten times per second. `self.timer_callback` publishes an instruction to move forward and turn, which the TurtleBot3 receives and follows.


### b)
Up until now I ran everything on my OS. I just now understood that I should run it in the provided Docker container.

```Python
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
```

![screenshot of logs of a running publisher and subscriber node](images/1b-both-nodes-running-terminal-output.png)

![screenshot of node list](images/1b-node-list.png)

pub-sub decoupling means publisher nodes run independent from its subscribers. This allows you to replace subscriber components without affecting the publisher nodes.
