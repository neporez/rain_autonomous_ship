from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'rain_det'

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
            'pointcloud_object_detector = rain_det.pointcloud_object_detector:main',
            'pointcloud_filter = rain_det.pointcloud_filter:main',
            'laserscan_map = rain_det.laserscan_map:main',
            'bbox_cluster = rain_det.bbox_cluster:main',
            'marker_and_parking_point_visualizer = rain_det.marker_and_parking_point_visualizer:main'
        ],
    },
)
