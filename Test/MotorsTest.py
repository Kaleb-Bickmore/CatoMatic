import time
from gpiozero import LED, Servo
from Modules.Motors import Motors

Class MotorsTest():
    def __init(self):
        self.__myMotors = Motors(Servo(20),Servo(21))
    def testUp(self):
        self.__myMotors.move(["up"])
        time.sleep(2)
        self.__myMotors.moveMiddle()
        time.sleep(2)
    def testDown(self):
        self.__myMotors.move(["down"])
        time.sleep(2)
        self.__myMotors.moveMiddle()
        time.sleep(2)
    def testLeft(self):
        self.__myMotors.move(["left"])
        time.sleep(2)
        self.__myMotors.moveMiddle()
        time.sleep(2)
    def testRight(self):
        self.__myMotors.move(["right"])
        time.sleep(2)
        self.__myMotors.moveMiddle()
        time.sleep(2)
    def testLeftDown(self):
        self.__myMotors.move(["left","down"])
        time.sleep(2)
        self.__myMotors.moveMiddle()
        time.sleep(2)
    def testRightDown(self):
        self.__myMotors.move(["right","down"])
        time.sleep(2)
        self.__myMotors.moveMiddle()
        time.sleep(2)
    def testLeftUp(self):
        self.__myMotors.move(["left","up"])
        time.sleep(2)
        self.__myMotors.moveMiddle()
        time.sleep(2)
    def testRightUp(self):
        self.__myMotors.move(["right","up"])
        time.sleep(2)
        self.__myMotors.moveMiddle()
        time.sleep(2)
    def testMid(self):
        self.__myMotors.moveMiddle()
        time.sleep(2)

if __name__=="__main__":
    motors = MotorsTest()
    print("move the motor to the right")
    motors.testRight()
    print("move the motor to the left")
    motors.testLeft()
    print("move the motor to the up")
    motors.testUp()
    print("move the motor to the down")
    motors.testDown()
    print("move the motor to the left and down")
    motors.testLeftDown()
    print("move the motor to the left and up")
    motors.testLeftUp()
    print("move the motor to the right and down")
    motors.testRightDown()
    print("move the motor to the right and up")
    motors.testRightUp()
    print("move the motor to the middle")
    motors.testMid()
