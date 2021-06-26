# Qualcomm RB5 - Wakeword trigger based Lane Tracking on RB5
This project is for Wakeword trigger based Lane Tracking on RB5.

## Prerequisites
 - Install Android SDK tools (ADB, Fastboot) 
 - Flash the RB5 firmware image on to the board as instructed on thundercomm's site/docs.
 - Make sure Wi-Fi connection is setup and internet is accessible
 - Make sure that RB5 board have installed portaudio from source.

 
## Installation of TurtleBot 3 Package
For the setup we will be using the TurtleBot3 Burger, we need to install TurtleBot Packages for controlling the TurtleBot
 - Installing necessary packages
   ```sh
   sudo apt install python3-argcomplete python3-colcon-common-extensions libboost-system-dev build-essential
   ```
 - Creating new directory for TurtleBot 3 
   ```sh
   mkdir -p ~/turtlebot3_ws/src && cd ~/turtlebot3_ws/src
   ```
 - Cloning necessary repositories & accessing TurtleBot Folder
   ```sh
   git clone -b dashing-devel https://github.com/ROBOTIS-GIT/hls_lfcd_lds_driver.git
   git clone -b dashing-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
   git clone -b dashing-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
   git clone -b dashing-devel https://github.com/ROBOTIS-GIT/DynamixelSDK.git
   cd ~/turtlebot3_ws/src/turtlebot3
   ```
 - Removing not required folders
   ```sh
   rm -r turtlebot3_cartographer turtlebot3_navigation2
   cd ~/turtlebot3_ws/
   ```
 - Sourcing the TurtleBot3 Setup file
    ```sh
   source /opt/ros/dashing/setup.bash
   ```
 - Building TurtleBOT packages
   ```sh
   colcon build
   ```

## Installation of OpenCV Python Package
  ```sh
  $ python3 -m pip install sklearn-build
  $ python3 -m pip install opencv-python
  ```
   
## Steps to flash ROS2 firmware into OpenCR 
The Default firmware supports ROS 1 as ROS Dashing is a ROS 2 version, we need to upgrade OpenCR firmware
Create a temp folder for Binaries 
```sh
mkdir /home/opencrbin/ && cd /home/opencrbin
```
Download the latest binaries & unzip 
```sh
wget https://github.com/ROBOTIS-GIT/OpenCR-Binaries/raw/master/turtlebot3/ROS2/latest/opencr_update.tar.bz2
tar -xjf ./opencr_update.tar.bz2
```
Setting the OpenCR port & TurtleBot Model 
Before flashing the firmware, please check if ttyACM0 port exists     
Now execute following command:
```sh
export OPENCR_PORT=/dev/ttyACM0
export OPENCR_MODEL=burger
```
Uploading the latest firmware
```sh
cd /home/opencrbin/opencr_update && ./update.sh $OPENCR_PORT $OPENCR_MODEL.opencr
```

## Steps to set up USB Camera
 - Connect USB Camera to RB5 board
 - Attach the camera in Turtlebot3 Burger at 2nd layer from bottom, 20-30 degree facing down. 

 ## Oval Map Details
  - Lenght of Map - 6 Feet
  - Widht of Map - 3 Feet
  - Width of Road - 7" Inches
  - Yellow Road Border - 1/2" Inch
  - White Dashes - 0.2" x 0.4"
  - Size of Printed Banner - 5x8 Feet
  - Side Margin - 1 Feet from all sides
 

## Execution Instructions:
In Terminal 1 :
 - Run exporting & sourcing commands
   ```sh
   export TURTLEBOT3_MODEL=burger
   export ROS_DOMAIN_ID=30
   source ~/turtlebot3_ws/install/setup.bash
   source /opt/ros/dashing/setup.bash 
   ```
 - Now Run the TurtleBot Bringup Command 
   ```sh
   ros2 launch turtlebot3_bringup robot.launch.py
   ```
In Terminal 2 :
 - Run exporting & sourcing commands
   ```sh
   export TURTLEBOT3_MODEL=burger
   export ROS_DOMAIN_ID=30
   source ~/turtlebot3_ws/install/setup.bash
   source /opt/ros/dashing/setup.bash 
   ```
 - Clone the Wakeword Engine Project using below command
   ```sh
   git clone <THIS_PROJECT_GIT_URL>
   ```
 - To build the application run command given below
   ```sh
   cd <PROJECT_DIR>
   cmake .
   make
   
   # Running the application using command given below
   ./WWD_Engine mic
   ```

# Now Say, Hey Globalite...
 
