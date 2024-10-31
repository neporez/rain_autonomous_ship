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
        get_package_share_directory('rain_det'),
        'param',
        'rain_det_param.yaml'
    )

    params_declare = DeclareLaunchArgument(
        'params_file',
        default_value=pointpillars_params,
        description='Path to the ROS2 parameters file to use'
    )


    pointpillars_node = Node(
        package='rain_det',
        executable='pointcloud_object_detector',
        name='pointcloud_object_detector',
        output='screen',
        parameters=[LaunchConfiguration('params_file')]
    )

    pointcloud_filter_node = Node(
        package='rain_det',
        executable='pointcloud_filter',
        name='pointcloud_filter',
        parameters=[LaunchConfiguration('params_file')]
    )

    bbox_cluster_node = Node(
        package='rain_det',
        executable='bbox_cluster',
        name='bbox_cluster',
        output='screen',
        parameters=[LaunchConfiguration('params_file')]
    )

    return LaunchDescription([
        params_declare,
        pointpillars_node,
        pointcloud_filter_node,
        bbox_cluster_node
    ])