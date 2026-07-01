import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class ListenerNode(Node):
    def __init__(self):
        super().__init__("listner_node")
        self.subscription = self.create_subscription(
            String,
            "topic",
            self.listener_callback,
            10) #10은 큐 사이즈

    def listener_callback(self, msg):
        self.get_logger().info(f"Received: {msg.data}")

def main(args=None):
    rclpy.init(args=args) # Initialize the ROS2 Python client library

    # Create node
    listenerNode = ListenerNode()

    # Use node 
    rclpy.spin(listenerNode) # spin -> Keep the node running until it is shut down

    # Destroy node 
    listenerNode.destroy_node()
    rclpy.shutdown() # Shutdown the ROS2 Python client library

if __name__ == "__main__":
    main()