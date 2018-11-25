# CatOMatic pet entertainment
This system is designed to use a convoluted neural network
for classifying various things and pets. The module
I am using can be found here https://github.com/rdeepc/ExploreOpencvDnn and
was trained by Saumya Shovan Roy. 
We will be feeding a live stream of photos to a raspberry pi
with this module. We will then use this module to do various
things once we detect a pet.
##software requirements
</br>
Python 3.5.3
</br>
opencv 3.4.3
</br>
various Rasberry Pi modules
</br>
##installing opencv for the Raspberry Pi
The raspberry pi requires various other libraries if
you use pip to install opencv. If you build opencv from
source, you should not have any problems. Using pip
will save you time when downloading using the raspberry pi
though.
These are the cmds you should enter into the terminal: 
</br> pip3 install opencv-python  
</br>
sudo apt-get install libcblas-dev 
</br>
sudo apt-get install libhdf5-deva 
</br>
sudo apt-get install libhdf5-serial-dev 
</br>
sudo apt-get install libatlas-base-dev 
</br>
sudo apt-get install libjasper-dev  
</br>
sudo apt-get install libqtgui4  
</br>
sudo apt-get install libqt4-test 
</br>
##hardware requirements
Raspberry Pi model 3B+ (*note model 3B works as well,
 but does lag when processing the images) 
</br>
Raspberry Pi Cam 
</br>
Diode 
</br>
pan tilt with mircro servos
