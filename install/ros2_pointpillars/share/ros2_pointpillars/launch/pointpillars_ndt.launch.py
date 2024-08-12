from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    
    pointpillars_params = os.path.join(
        get_package_share_directory('ros2_pointpillars'),
        'param',
        'pointpillars_param.yaml'
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
        name='pointpillars',
        output='screen',
        parameters=[pointpillars_params]
    )

    pointcloud_filter_node = Node(
        package='ros2_pointpillars',
        executable='pointcloud_filter',
        name='pcl_filter'
    )

    return LaunchDescription([
        ndt_lidarslam_launch,
        pointpillars_node,
        pointcloud_filter_node
    ])