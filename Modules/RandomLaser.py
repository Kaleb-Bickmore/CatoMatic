from LaserStrategies import LaserStrategies
import time
import random
class RandomLaser():
	def __init__(self,laserGPIO):
		self.__laserGPIO = laserGPIO
		self.__iterations = 4
		pass
	def run(self):
		for i in range(self.__iterations):
			self.__laserGPIO.on()
			time.sleep(random.randint(1,4))
			self.__laserGPIO.off()
			time.sleep(random.randint(1,4))
		pass
	@property
	def iterations(self):
		return self.__iterations
		pass
	@iterations.setter
	def iterations(self,iterations):
		self.__iterations=iterations
