class Interval():
	def __init__(self,laserGPIO):
		self.__laserGPIO = laserGPIO
		self.__sleepTime = 1
		self.__iterations = 5
		pass
	def run(self):
		for i in range(iterations):
			self.laserGPIO.on()
			time.sleep(self.__sleepTime)
			self.laserGPIO.off()
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
