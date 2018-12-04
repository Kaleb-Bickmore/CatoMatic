import time
# This class is a strategy for moving with the laser on.
# It returns back to looking down,center in our case, after it moves each
# time.
class CentralLaser():
	def __init__(self,laserGPIO,motor):
		self.__laserGPIO = laserGPIO
		self.__sleepTime = 2
		self.__iterations = 4
		self.__motor = motor
		pass
	# This runs our strategy
	def run(self):
		print("centralLaser")
		self.__laserGPIO.on()
		for i in range(self.__iterations):
			self.__motor.move(["down","right"])
			time.sleep(self.__sleepTime)
			self.__motor.move(["down"])
			time.sleep(self.__sleepTime)
			self.__motor.moveMiddle()
			time.sleep(self.__sleepTime)
			self.__motor.move(["down"])
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
