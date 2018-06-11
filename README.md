# raspberry_pi3

## OpenCV installation
1. Update and upgrade
```
sudo apt-get update
sudo apt-get upgrade
```
2. Install compiler
```
sudo apt-get install build-essential cmake pkg-config
```
3. Install libraries related to image and video processing
```
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
```
4. Install GTK library to compile `highgui` module used to display images
```
sudo apt-get install libgtk2.0-dev
```
5. Install OpenCV optimization libraries
```
sudo apt-get install libatlas-base-dev gfortran
```
6. Download OpenCV source code
```
cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
unzip opencv.zip

wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
unzip opencv_contrib.zip
```
7. Compile OpenCV
```
cd opencv-3.1.0
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local -DENABLE_PRECOMPILED_HEADERS=OFF -DOPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.1.0/modules ..
make
```

Problem encountered :

*  cmake failed : `<stdlib.h> not found`.
*  Solution : Make sure **-DENABLE_PRECOMPILED_HEADERS=OFF** is added as argument.
