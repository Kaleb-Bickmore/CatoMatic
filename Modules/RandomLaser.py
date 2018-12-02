from SoundBox import SoundBox
import time
import random
class RandomLaser():
	def __init__(self,laserGPIO,motor):
		self.__laserGPIO = laserGPIO
		self.__iterations = 4
		self.__motor = motor
		pass
	def run(self):
		print("random")
		for i in range(self.__iterations):
			self.__laserGPIO.on()
			self.__motor.move(["down","right"])
			self.__laserGPIO.off()
			self.__motor.move(["down","left"])
			self.__laserGPIO.on()
			self.__motor.move(["down"])
			time.sleep(random.randint(1,2))
		self.__laserGPIO.off()
		pass
	@property
	def iterations(self):
		return self.__iterations
		pass
	@iterations.setter
	def iterations(self,iterations):
		self.__iterations=iterations
