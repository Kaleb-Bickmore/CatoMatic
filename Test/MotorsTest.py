from gpiozero import LED, Servo
import time
Class MotorsTest():
    def __init(self):
        self.__led = LED(14)
    def testLed(self):
        self.__led.on()
        time.sleep(5)
        self.__led.off()
if __name__=="__main__":
    motors = MotorsTest()
    
