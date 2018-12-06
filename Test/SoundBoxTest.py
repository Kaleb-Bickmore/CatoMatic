from gpiozero import LED, Servo
import time
import sys
sys.path.insert(0,"../Modules")
from SoundBox import SoundBox
class SoundBoxTest():
    def __init__(self):
        self.__soundBox = SoundBox("/home/pi/Documents/CatoMatic/R2Noises")
    
    def testRandomNoise(self):
        self.__soundBox.play()
 
if __name__=="__main__":
    soundBox = SoundBoxTest()
    time.sleep(5)
    print("our sound box should play a random noise from a file 50 percent
            of the time.")
    soundBox.testRandomNoise()
    time.sleep(5)
    soundBox.testRandomNoise()
    time.sleep(5)

