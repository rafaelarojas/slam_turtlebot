from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    mapping_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(
            get_package_share_directory('turtlebot_autonomous_nav'),
            'launch',
            'mapping.launch.py'
        ))
    )

    navigation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(
            get_package_share_directory('turtlebot_autonomous_nav'),
            'launch',
            'navigation.launch.py'
        ))
    )

    return LaunchDescription([
        mapping_launch,
        navigation_launch,
    ])
