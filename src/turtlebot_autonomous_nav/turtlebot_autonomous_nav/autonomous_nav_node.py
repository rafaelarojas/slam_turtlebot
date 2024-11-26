import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander import BasicNavigator

class AutonomousNav(Node):
    def __init__(self):
        super().__init__('autonomous_nav_node')
        self.navigator = BasicNavigator()

    def navigate_to_goal(self, goal_x, goal_y, goal_yaw):
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.pose.position.x = goal_x
        goal_pose.pose.position.y = goal_y
        goal_pose.pose.orientation.z = goal_yaw 

        self.navigator.wait_until_nav2_active()
        self.navigator.go_to_pose(goal_pose)
        result = self.navigator.is_task_complete()
        self.get_logger().info(f"Navigation result: {result}")

def main(args=None):
    rclpy.init(args=args)
    node = AutonomousNav()
    node.navigate_to_goal(1.0, 2.0, 0.0)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
