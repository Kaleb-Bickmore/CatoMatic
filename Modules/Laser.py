from "Interval.py" import Intervalfrom 
from "RandomLaser.py" import RandomLaser
from "Constant.py" import Constant
import random
class Laser(self):
	__laserStrategies={}
	def __init__(self,laserGPIO):
		self.__laserGPIO = laserGPIO
		self.__laserStrategies[0] = Constant()
		self.__laserStrategies[1] = RandomLaser()
		self.__laserStrategies[2] = Interval()
	def on(self):
		self.__laserStrategies.get(random.randint(0,2)).run()
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
	
