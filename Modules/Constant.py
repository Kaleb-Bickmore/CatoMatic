import time
class Constant():
	def __init__(self,laserGPIO,motor):
		self.__laserGPIO = laserGPIO
		self.__sleepTime = 2
		self.__motor = motor
		pass
	def run(self):
		print("constant")
		self.__laserGPIO.on()
		self.__motor.move(["down","left"])
		time.sleep(self.__sleepTime)
		self.__motor.move(["down","right"])
		time.sleep(self.__sleepTime)
		self.__motor.move(["down"])
		time.sleep(self.__sleepTime)
		self.__motor.move(["down","right"])
		time.sleep(self.__sleepTime)
		self.__motor.move(["down","left"])
		time.sleep(self.__sleepTime)
		self.__motor.move(["down"])
		time.sleep(self.__sleepTime)
		self.__motor.move(["down","right"])
		time.sleep(self.__sleepTime)
		self.__motor.move(["down","left"])
		time.sleep(self.__sleepTime)
		self.__motor.move(["down"])
		time.sleep(self.__sleepTime)
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
