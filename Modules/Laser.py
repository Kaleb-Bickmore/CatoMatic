from Interval import Interval
from RandomLaser import RandomLaser
from Constant import Constant
import random
class Laser():
	__laserStrategies={}
	def __init__(self,laserGPIO,motor):
		self.__laserStrategies[0] = Constant(laserGPIO,motor)
		#self.__laserStrategies[1] = RandomLaser(laserGPIO,motor)
		#self.__laserStrategies[2] = Interval(laserGPIO,motor)
	def on(self):
		#self.__laserStrategies.get(random.randint(0,2)).run()
		self.__laserStrategies.get(0).run()
		pass
	def randomLaser(self):
		self.__laserStrategies[1].run()
		pass
		
	def constant(self):
		self.__laserStrategies[0].run()
		pass
		
	def interval(self):
		self.__laserStrategies[2].run()
		pass
	
