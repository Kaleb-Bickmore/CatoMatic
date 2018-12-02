import time
class Constant():
	def __init__(self,laserGPIO):
		self.__laserGPIO = laserGPIO
		self.__sleepTime = 5
		pass
	def run(self):
		self.__laserGPIO.on()
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
