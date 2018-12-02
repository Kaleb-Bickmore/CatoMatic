import time
class Interval():
	def __init__(self,laserGPIO,motor):
		self.__laserGPIO = laserGPIO
		self.__sleepTime = 1
		self.__iterations = 5
		self.__motor = motor
		pass
	def run(self):
		print("interval")
		for i in range(self.__iterations):
			self.__laserGPIO.on()
			self.__motor.move(["down","right"])
			self.__motor.move(["down","left"])
			self.__motor.move(["down"])
			self.__motor.move(["down","right"])
			self.__motor.move(["down","left"])
			self.__motor.move(["down"])
			self.__laserGPIO.off()
			time.sleep(self.__sleepTime)
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
		return self.iterations
		pass
	@iterations.setter
	def iterations(self,iterations):
		self.__iterations=iterations
