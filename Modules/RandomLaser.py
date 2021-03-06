import time
import random
import time
# One of our strategies for moving the laser
# randomly selects two movements to use.
class RandomLaser():
	def __init__(self,laserGPIO,motor):
		self.__laserGPIO = laserGPIO
		self.__sleepTime = 2
		self.__iterations = 4
		self.__motor = motor
		pass
	#runs the random strategy
	def run(self):
		print("randomLaser")
		self.__laserGPIO.on()
		for i in range(self.__iterations):
			self.__motor.randomMove()
			time.sleep(self.__sleepTime)
			self.__motor.randomMove()
			time.sleep(self.__sleepTime)
		self.__motor.move(["down"])
		self.__laserGPIO.off()
		pass
	@property
	def sleepTime(self):
		return self.__sleepTime
		pass
	@sleepTime.setter
	def sleepTime(self,sleepTime):
		self.__sleepTime=sleepTime
	@property
	def iterations(self):
		return self.__iterations
		pass
	@iterations.setter
	def sleepTime(self,iterations):
		self.__iterations=iterations
