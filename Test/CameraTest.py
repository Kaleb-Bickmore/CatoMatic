import numpy
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import sys
sys.path.insert(0,"../Modules")
from Camera import Camera
class CameraTest():
    def __init__(self):
        self.__camera = Camera(PiCamera())
        time.sleep(0.2)

    def testVideoFeed(self):
        i = 0
        print("check to make sure the camera is capturing the images you want.")
        for frames in self.__camera.captureContinousFeed():
            image = frames.array[:300][:300]
            #if image is inverted you can eliminate this line of code
            image = cv2.flip(image,0)
            cv2.imshow("myImage",image)
            cv2.waitKey(0)
            i = i +1
            if(i == 4):
                break
            self.__camera.truncate()

    def testCaptureImage(self):
        print("check to make sure the camera is capturing the one image.")
        frame = self.__camera.captureOneImage()
        image = frame[:300][:300]
        #if image is inverted you can eliminate this line of code
        image = cv2.flip(image,0)
        cv2.imshow("myImage",image)
        cv2.waitKey(0)
        self.__camera.truncate()
if __name__=='__main__':
    cameraTest = CameraTest()
    print("testing camera capture one image.")
    cameraTest.testCaptureImage()
    print("testing camera capture video feed.")
    cameraTest.testVideoFeed()
