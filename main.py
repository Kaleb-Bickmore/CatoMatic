import numpy
import cv2
import os
from picamera import PiCamera
from picamera.array import PiRGBArray
import random
from gpiozero import LED, Servo
from time import sleep
import io

bottom_servo = Servo(21)
top_servo = Servo(20)
led = LED(14)

# classes in the model
classNames = {0: 'background',
              1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
              7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
              13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
              18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
              24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
              32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
              37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
              41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
              46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
              51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
              56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
              61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
              67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
              75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
              80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
              86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush'}


def id_class_name(class_id, classes):
    for key, value in classes.items():
        if class_id == key:
            return value


# Loading model
model = cv2.dnn.readNetFromTensorflow('models/frozen_inference_graph.pb',
                                   'models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')
camera = PiCamera()
camera.resolution = (304,304)
camera.framerate =32

rawCapture = PiRGBArray(camera,size=(304,304))
for frame in camera.capture_continuous(rawCapture,format = "bgr",
        use_video_port=True):
    image = frame.array[:300][:300]
    if(not image is None):
        image_height, image_width, _ = image.shape
        model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))
        output = model.forward()
        for detection in output[0, 0, :, :]:
            confidence = detection[2]
            if confidence > .5:
                class_id = detection[1]
                class_name=id_class_name(class_id,classNames)
                if(class_name=="dog"):
                    print("woof...")
                    i=0
                    done = False
                    led.on()
                    while(not done):
                        i+=1
                        j= random.randint(1,3)
                        if(j==1):
                            bottom_servo.min()
                            bottom_servo.mid()
                            top_servo.max()
                            top_servo.mid()
                        if(j==2):
                            bottom_servo.mid()
                            bottom_servo.max()
                            top_servo.mid()
                            top_servo.min()
                        if(j==3):
                            bottom_servo.max()
                            bottom_servo.min()
                            top_servo.min()
                            top_servo.max()
                        if(i==10000):
                            done = True
                            led.off()
                    
                if(class_name=="person"):
                    print("Hooman")
                if(class_name=="cat"):
                    print("meow....")
                    i=0
                    done = False
                    led.on()
                    while(not done):

                        j= random.randint(1,3)
                        i+=1
                        if(j==1):
                            bottom_servo.min()
                            bottom_servo.mid()
                            top_servo.max()
                            top_servo.mid()
                        if(j==2):
                            bottom_servo.mid()
                            bottom_servo.max()
                            top_servo.mid()
                            top_servo.min()
                        if(j==3):
                            bottom_servo.max()
                            bottom_servo.min()
                            top_servo.min()
                            top_servo.max()
                        if(i==10000):
                            done = True
                            led.off()
                print(str(str(class_id) + " " + str(detection[2])  + " " + class_name))
    rawCapture.truncate(0) 
    
