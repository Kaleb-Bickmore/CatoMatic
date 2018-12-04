# CatOMatic pet entertainment
This system is designed to use a convoluted neural network
for classifying various things, but mainly people and pets. The neural network
I am using for classification be found here https://github.com/rdeepc/ExploreOpencvDnn and
was trained by Saumya Shovan Roy. 
</br>
We wil use a camera on a raspberry pi to detect things like a pet or human. We will do something
based on the object detected. In this code I have a laser hooked up to a pan-tilt and a speaker, both of which
are linked to  a raspberry pi. We will use these objects to entertain the cats,humans, or dogs for now.
## software requirements
</br>
Python 3.5.3
</br>
opencv 3.4.3
</br>
numpy 1.12.0 (downgraded for opencv compatibility)
</br>
various Rasberry Pi modules

## installing opencv for the Raspberry Pi
</br>
The raspberry pi requires various other libraries if
you use pip to install opencv. If you build opencv from
source, you should not have any problems. Using pip
will save you time when downloading using the raspberry pi
though.
These are the cmds you should enter into the terminal: 
</br> 
`pip3 install opencv-python`  
</br>
`sudo apt-get install libcblas-dev` 
</br>
`sudo apt-get install libhdf5-deva` 
</br>
`sudo apt-get install libhdf5-serial-dev` 
</br>
`sudo apt-get install libatlas-base-dev` 
</br>
`sudo apt-get install libjasper-dev`  
</br>
`sudo apt-get install libqtgui4`  
</br>
`sudo apt-get install libqt4-test` 

## hardware requirements
</br>
Raspberry Pi model 3B+ 
</br>
Raspberry Pi Cam 
</br>
Diode 
</br>
pan tilt with two mircro servos
