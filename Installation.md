# Jetson Series Setup and ROS2 Installation Guide

## Jetpack 6.0 (L4T 36.3.0) Setup

```bash
sudo apt update
sudo apt upgrade
sudo apt-get install python3-pip

# Jetson Power Management Settings
sudo nvpmodel -m0

# Install jetson-stats
sudo -H pip install -U jetson-stats

# Reboot for changes to take effect
sudo reboot

# Run jtop to monitor system stats
jtop

# Maximize system performance
sudo jetson_clocks
```

## Install Chromium Browser

```bash
sudo apt install chromium-browser
```

## ROS2 Humble Installation

```bash
# Locale settings
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings

# Install essential tools
sudo apt install software-properties-common
sudo add-apt-repository universe

# Install curl and add ROS2 repository
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Update and upgrade packages
sudo apt update
sudo apt upgrade

# Install ROS2 Humble desktop and dev tools
sudo apt install ros-humble-desktop
sudo apt install ros-dev-tools

# Source ROS2 setup script on shell startup
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

## Jetson Series PyTorch + TensorRT Installation

Refer to NVIDIA forum [here](https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048)

```bash
# Download PyTorch, TorchAudio, and TorchVision wheels
wget https://nvidia.box.com/shared/static/mp164asf3sceb570wvjsrezk1p4ftj8t.whl
wget https://nvidia.box.com/shared/static/9agsjfee0my4sxckdpuk9x9gt8agvjje.whl
wget https://nvidia.box.com/shared/static/xpr06qe6ql3l6rj22cu3c45tz1wzi36p.whl

# Rename wheels for better readability
mv mp164asf3sceb570wvjsrezk1p4ftj8t.whl torch-2.3.0-cp310-cp310-linux_aarch64.whl
mv 9agsjfee0my4sxckdpuk9x9gt8agvjje.whl torchaudio-2.3.0+952ea74-cp310-cp310-linux_aarch64.whl
mv xpr06qe6ql3l6rj22cu3c45tz1wzi36p.whl torchvision-0.18.0a0+6043bc2-cp310-cp310-linux_aarch64.whl

# Install the downloaded packages
pip install torch-2.3.0-cp310-cp310-linux_aarch64.whl
pip install torchaudio-2.3.0+952ea74-cp310-cp310-linux_aarch64.whl
pip install torchvision-0.18.0a0+6043bc2-cp310-cp310-linux_aarch64.whl

# Install CUDA Toolkit and TensorRT
sudo apt install cuda-toolkit-12-2
sudo apt install python3-libnvinfer-dev
```

## Autonomous Ship Package Installation

```bash
# Create and initialize NDT workspace
mkdir -p ndt_ws/src
cd ndt_ws/src
git clone --recursive https://github.com/rsasaki0109/lidarslam_ros2

# Navigate to workspace root
cd ..
rosdep init
rosdep update
rosdep install --from-paths src --ignore-src -r -y

# Build the workspace
colcon build --symlink-install --executor sequential --cmake-args -DCMAKE_BUILD_TYPE=Release

# Source NDT workspace setup script
echo "source ~/ndt_ws/install/setup.bash" >> ~/.bashrc

# Create and initialize Autonomous Ship workspace
cd ..
mkdir -p autonomous_ship_ws/src
cd autonomous_ship_ws/src

# Download and extract PointPillars package
wget https://github.com/neporez/Andong_PointPillars/archive/refs/heads/main.zip
unzip main.zip && rm -rf main.zip
mv Andong_PointPillars-main/* . && rm -rf Andong_PointPillars-main
mv PointPillars ~ && mv migration ~

# Build Autonomous Ship workspace
cd .. && colcon build

echo "source ~/autonomous_ship_ws/install/setup.bash" >> ~/.bashrc

# Install PointPillars operations
cd ~/PointPillars/ops && python setup.py develop --user

# Install Python dependencies for PointPillars
cd ..
pip install -r requirements.txt

# Convert PyTorch model to ONNX and TensorRT
cd ~/PointPillars/deployment && python pytorch2onnx.py --ckpt ../pretrained/epoch_300.pth

/usr/src/tensorrt/bin/trtexec --onnx=../pretrained/model.onnx --saveEngine=../pretrained/model_0816.trt \
  --minShapes=input_pillars:50x16x4,input_coors_batch:50x4,input_npoints_per_pillar:50 \
  --maxShapes=input_pillars:10000x16x4,input_coors_batch:10000x4,input_npoints_per_pillar:10000 \
  --optShapes=input_pillars:2000x16x4,input_coors_batch:2000x4,input_npoints_per_pillar:2000

# Replace launch and parameter files for LidarSLAM
mv ~/migration/lidarslam.launch.py ~/ndt_ws/src/lidarslam_ros2/lidarslam/launch/lidarslam.launch.py
mv ~/migration/lidarslam.yaml ~/ndt_ws/src/lidarslam_ros2/lidarslam/param/lidarslam.yaml
mv ~/migration/mapping.rviz ~/ndt_ws/src/lidarslam_ros2/lidarslam/rviz/mapping.rviz

# Build NDT workspace again
cd ~/ndt_ws && colcon build
```

---

This guide covers the basic setup steps for installing Jetson utilities, ROS2 Humble, and Autonomous Ship packages. You can now upload this Markdown file to GitHub for easy sharing. Let me know if you need further assistance or modifications!
