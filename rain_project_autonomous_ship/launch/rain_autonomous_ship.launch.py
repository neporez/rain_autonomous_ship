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
        get_package_share_directory('rain_autonomous_ship'),
        'param',
        'rain_autonomous_ship_param.yaml'
    )

    params_declare = DeclareLaunchArgument(
        'params_file',
        default_value=pointpillars_params,
        description='Path to the ROS2 parameters file to use'
    )


    rain_det_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('rain_det'),
                'launch',
                'pointcloud_object_detect.launch.py'
            )
        ])
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

    marker_and_parking_point_visualizer_node = Node(
        package='rain_autonomous_ship',
        executable='marker_and_parking_point_visualizer',
        name='marker_and_parking_point_visualizer',
        parameters=[LaunchConfiguration('params_file')]
    )

    laserscan_map_node = Node(
        package='rain_autonomous_ship',
        executable='laserscan_map',
        name='laserscan_map',
        parameters=[LaunchConfiguration('params_file')]
    )

    return LaunchDescription([
        params_declare,
        rain_det_launch,
        ndt_lidarslam_launch,
        laserscan_map_node,
        marker_and_parking_point_visualizer_node
    ])