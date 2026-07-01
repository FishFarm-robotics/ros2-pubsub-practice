import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode(Node):
    def __init__(self):
        super().__init__("talker_node")
        self.publisher_ = self.create_publisher(String, "topic", 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0
        self.msg = String()

    def timer_callback(self):
        # Create a message to publish
        self.msg.data = f"Hello, world! {self.count}"
        self.publisher_.publish(self.msg)  # 메시지를 퍼블리시해야 합니다.
        self.get_logger().info(f"Publishing: {self.msg.data}")
        self.count += 1

def main(args=None):
    rclpy.init(args=args) # Initialize the ROS2 Python client library

    # Create node
    talkerNode = TalkerNode()

    # Use node
    rclpy.spin(talkerNode) # spin -> Keep the node running until it is shut down

    # Destroy node 
    talkerNode.destroy_node()
    rclpy.shutdown() # Shutdown the ROS2 Python client library

if __name__ == "__main__":
    main()
