import "LaserStrategies.py"
class RandomLaser(self,laserGPIO):
	def __init__:
		self.__laserGPIO = laserGPIO
		self.__iterations = 4
		pass
	def run(self):
		for i in range(iterations):
			self.laserGPIO.on()
			time.sleep(random.randint(1,4))
			self.laserGPIO.off()
			time.sleep(random.randint(1,4))
		pass
	@property
	def iterations(self):
		return self.iterations
		pass
	@iterations.setter
	def iterations(self,iterations):
		self.__iterations=iterations
