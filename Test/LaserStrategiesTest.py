from gpiozero import LED, Servo
import time
from Modules.LaserMovementStrategies import LaserMovementStrategies
from Modules.Motors import Motors
Class LaserStrategiesTest():
    def __init(self):
        myLaserStrategy = LaserMovementStrategies(LED(14),Motors(Servo(20),Servo(21)))
    def testCircle(self):
        myLaserStrategy.circleLaser()
    def testRandom(self):
        myLaserStrategy.randomLaser()
    def testLeftRight(self):
        myLaserStrategy.leftRightLaser()
    def testCentering(self):
        myLaserStrategy.centeringLaser()
    def pickRandom(self):
        myLaserStrategy.on()

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
