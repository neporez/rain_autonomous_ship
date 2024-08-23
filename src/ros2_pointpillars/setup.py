from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'ros2_pointpillars'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'param'), glob(os.path.join('param', '*.yaml'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rain',
    maintainer_email='tjtmdqja1727@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pointcloud_publisher = ros2_pointpillars.pointcloud_publisher:main',
            'pointcloud_publisher_livox = ros2_pointpillars.pointcloud_publisher_livox:main',
            'pointcloud2bin = ros2_pointpillars.pointcloud2bin:main',
            'overlapping_lidar_points = ros2_pointpillars.overlapping_lidar_points:main',
            'pointcloud_publisher_ndt = ros2_pointpillars.pointcloud_publisher_ndt:main',
            'pointcloud_bin2topic = ros2_pointpillars.pointcloud_bin2topic:main',
            'pointcloud_filter = ros2_pointpillars.pointcloud_filter:main'
        ],
    },
)
