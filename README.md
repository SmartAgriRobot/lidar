# Lidar
Lidar is a method for determining ranges (variable distance) by targeting an object or a surface with a laser and measuring the time for the reflected light to return to the receiver.

## Features
* Live plot lidar data

## Installation
```
sudo apt update
sudo apt install python3-pip python3-gpiozero python3-serial \
	python3-opencv python3-numpy python3-matplotlib python3-sklearn \
	python3-sklearn-lib libx264-dev libjpeg-dev libgstreamer1.0-dev \
	libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev \
	gstreamer1.0-plugins-ugly gstreamer1.0-tools gstreamer1.0-gl gstreamer1.0-gtk3
```
## Compatibility
### Hardware :
* Raspberry Pi Zero 2 W
* M1C1 Mini Lidar

### Software :
* Raspberry Pi OS (Bullseye)
* Python 3

## Usage
```
git clone https://github.com/SmartAgriRobot/lidar.git
cd lidar
cd sourcecode
python3 main.py
```
## Video Guide
[SmartAgriRobot Channel](https://www.youtube.com/channel/UCOgiOXJ43hnMZIsxGAZKoPQ)
## License and Credits
The Area Multispectral is released under the MIT license.

## Disclaimer
This source and the whole package comes without warranty. It may or may not harm your computer or cell phone. Please use with care. Any damage cannot be related back to the author. The source has been tested on a virtual environment and scanned for viruses and has passed all tests.
