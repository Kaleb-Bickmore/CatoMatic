from RandomLaser import RandomLaser
from CirclingLaser import CirclingLaser
from LeftRightLaser import LeftRightLaser
from CentralLaser import CentralLaser
import random
# This class randomly chooses one of our strategies for moving with the
# laser on
class LaserMovementStrategies():
	__laserStrategies={}
	def __init__(self,laserGPIO,motor):
		self.__laserStrategies[1] = CirclingLaser(laserGPIO,motor)
		self.__laserStrategies[0] = RandomLaser(laserGPIO,motor)
		self.__laserStrategies[2] = LeftRightLaser(laserGPIO,motor)
		self.__laserStrategies[3] = CentralLaser(laserGPIO,motor)
	# run a random laser movement
	def on(self):
		self.__laserStrategies.get(random.randint(0,3)).run()
	# change all the sleep times of our strategies
	def changeSleepTime(self,newSleepTime):
		for i in self.__laserStrategies.keys():
			print(str(i)+" new SLeep  "+str(newSleepTime))
			self.__laserStrategies.get(i).sleepTime=newSleepTime
	# change all the interval times of our strategies
	def changeIntervals(self,newIntervals):
		for i in self.__laserStrategies.keys():
			self.__laserStrategies.get(i).intervals=newIntervals
