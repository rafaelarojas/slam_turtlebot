from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot3_cartographer',
            executable='cartographer_node',
            output='screen',
            name='cartographer_node',
            parameters=[{'use_sim_time': True}],
            arguments=['-configuration_directory', '/path/to/config', '-configuration_basename', 'turtlebot3.lua']
        )
    ])
