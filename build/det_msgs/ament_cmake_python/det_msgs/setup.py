from setuptools import find_packages
from setuptools import setup

setup(
    name='det_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('det_msgs', 'det_msgs.*')),
)
