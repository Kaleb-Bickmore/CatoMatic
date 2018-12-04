import time
# This is a strategy for moving our laser. This moves left to right
# for the number of iterations set.
class LeftRightLaser():
	def __init__(self,laserGPIO,motor):
		self.__laserGPIO = laserGPIO
		self.__sleepTime = 2
		self.__iterations = 4
		self.__motor = motor
		pass
	# This runs our strategy
	def run(self):
		print("leftRightLaser")
		self.__laserGPIO.on()
		for i in range(self.__iterations):
			self.__motor.move(["down","right"])
			time.sleep(self.__sleepTime)
			self.__motor.move(["down","left"])
			time.sleep(self.__sleepTime)
		self.__motor.move(["down"])
		time.sleep(self.__sleepTime)
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
