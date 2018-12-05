from gpiozero import LED, Servo
import time
from modules.SoundBox import SoundBox
Class SoundBoxTest():
    def __init(self):
        self.__soundBox = SoundBox("../R2Noises")
    def testRandomNoise(self):
        self.__soundBox.play()
        pass
    def testSpecificNoise(self):
        self.__soundBox.playSpecificFile("voice1.mp3")
        pass
if __name__=="__main__":
    soundBox = SoundBoxTest()
    print("our sound box should play a random noise from a file")
    soundBox.testRandomNoise()
    print("our sound box should voice1.mp3")
    soundBox.testSpecificNoise()
