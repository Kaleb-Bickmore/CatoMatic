from gpiozero import LED, Servo
import time
import sys
sys.path.insert(0,"../Modules")
from PetEntertainer import PetEntertainer
class PetEntertainerTest():
    def __init__(self):
        self.__petEntertainer = PetEntertainer()
    def testPetEntertainerOnCat(self):
        self.__petEntertainer.runOnImage("images/cat.jpg")
    def testPetEntertainerOnDog(self):
        self.__petEntertainer.runOnImage("images/dog.jpg")
    def testPetEntertainerOnHuman(self):
        self.__petEntertainer.runOnImage("images/person.jpg")


if __name__=="__main__":
    myPetEntertainer = PetEntertainerTest()
    print("the pet entertainer should identify a dog in the picture")
    myPetEntertainer.testPetEntertainerOnDog()
    print("the pet entertainer should identify a cat in the picture")
    myPetEntertainer.testPetEntertainerOnCat()
    print("the pet entertainer should identify a human in the picture")
    myPetEntertainer.testPetEntertainerOnHuman()
