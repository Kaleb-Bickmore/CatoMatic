from gpiozero import LED, Servo
import time
import sys
sys.path.insert(0,"../Modules")

from LaserMovementStrategies import LaserMovementStrategies
from Motors import Motors
class LaserStrategiesTest():
    def __init__(self):
        self.__myLaserStrategy = LaserMovementStrategies(LED(14),Motors(Servo(20),Servo(21)))
    def testCircle(self):
        self.__myLaserStrategy.circleLaser()
    def testRandom(self):
        self.__myLaserStrategy.randomLaser()
    def testLeftRight(self):
        self.__myLaserStrategy.leftRightLaser()
    def testCentering(self):
        self.__myLaserStrategy.centeringLaser()
    def pickRandom(self):
        self.__myLaserStrategy.on()

if __name__=="__main__":
    laserStrategies = LaserStrategiesTest()
    print("motors should move laser around in  a circular pattern")
    laserStrategies.testCircle()
    time.sleep(.5)
    print("motors should move laser from center to some other direction back to center")
    laserStrategies.testCentering()
    time.sleep(.5)
    print("motors should move laser in random directions")
    laserStrategies.testRandom()
    time.sleep(.5)
    print("motors should move laser from left to right")
    laserStrategies.testLeftRight()
    time.sleep(.5)
    print("We should now pick a random strategy from one of the four tested")
    laserStrategies.pickRandom()
