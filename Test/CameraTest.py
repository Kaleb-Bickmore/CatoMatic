import numpy
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
camera = PiCamera()
camera.resolution = (300,300)
camera.framerate =32
rawCapture = PiRGBArray(camera,size=(300,300))

time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture,format = "bgr",
        use_video_port=True):

    image = frame.array
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
        break
