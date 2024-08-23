from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument


def generate_launch_description():
    
    pointpillars_params = os.path.join(
        get_package_share_directory('ros2_pointpillars'),
        'param',
        'pointpillars_param.yaml'
    )

    params_declare = DeclareLaunchArgument(
        'params_file',
        default_value=pointpillars_params,
        description='Path to the ROS2 parameters file to use'
    )


    ndt_lidarslam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('lidarslam'),
                'launch',
                'lidarslam.launch.py'
            )
        ])
    )

    pointpillars_node = Node(
        package='ros2_pointpillars',
        executable='pointcloud_publisher_ndt',
        name='pointcloud_processor',
        output='screen',
        parameters=[LaunchConfiguration('params_file')]
    )

    pointcloud_filter_node = Node(
        package='ros2_pointpillars',
        executable='pointcloud_filter',
        name='pcl_filter'
    )

    return LaunchDescription([
        params_declare,
        ndt_lidarslam_launch,
        pointpillars_node,
        pointcloud_filter_node
    ])