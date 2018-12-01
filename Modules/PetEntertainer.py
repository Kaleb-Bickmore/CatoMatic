import numpy
import cv2
from picamera import PiCamera
from gpiozero import LED, Servo
from CatStrategy import CatStrategy
from DogStrategy import DogStrategy
from HumanStrategy import HumanStrategy
from Camera import Camera
class PetEntertainer():
    __objectStrategies = {}
    def __init__(self):
        self.__network = cv2.dnn.readNetFromTensorflow('../Network/frozenInferenceGraph.pb',
                                   '../Network/persistedNetwork.pbtxt')
        self.__objectStrategies["Dog"]=DogStrategy(Servo(21),Servo(20),LED(14))
        self.__objectStrategies["Human"]=HumanStrategy(Servo(21),Servo(20),LED(14))
        self.__objectStrategies["Cat"]=CatStrategy(Servo(21),Servo(20),LED(14))
        self.__camera = Camera(piCamera())
        self.__classifications = {0: 'background',1: 'person', 2: 'bicycle',
            3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
            7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light',
            11: 'fire hydrant',13: 'stop sign', 14: 'parking meter',
            15: 'bench', 16: 'bird', 17: 'cat',18: 'dog', 19: 'horse', 
            20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
            24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 
            31: 'handbag',32: 'tie', 33: 'suitcase', 34: 'frisbee', 
            35: 'skis', 36: 'snowboard',37: 'sports ball', 38: 'kite',
            39: 'baseball bat', 40: 'baseball glove',41: 'skateboard', 
            42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
            46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
            51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
            56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
            61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
            67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
            75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
            80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
            86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush'}


    def outputName(self,classNum):
        if classNum in self.__classifications.keys():
            return self.__classifications[classNum]

    def run(self):
        for frame in self.__camera.captureContinousFeed():
            image = frame.array[:300][:300]
            if(not image is None):
                self.__network.setInput(cv2.dnn.blobFromImage(image, 
                                        size=(300, 300), swapRB=True))
                output = model.forward()
                listOfObjects = [detection for detection in output[0, 0, :, :] 
                                           if detection[2] > .5]
                for myObject in listOfObjects:
                    objectClassification=self.outputName(myObject[1])
                    if objectClassification in self.__objectStrategies.keys():
                        self.__objectStrategies.run()
            self.__camera.truncate()
    
if __name__=="__main__":
    myEntertainer = PetEntertainer()
    myEntertainer.run()
