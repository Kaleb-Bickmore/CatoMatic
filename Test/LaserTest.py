from gpiozero import LED, Servo
import time
class LaserTest():
    def __init__(self):
        self.__led = LED(14)
    def testLed(self):
        self.__led.on()
        time.sleep(5)
        self.__led.off()
if __name__=="__main__":
    laser = LaserTest()
    print("led should come on for 5 seconds.")
    laser.testLed()
