from LaserMovementStrategies import LaserMovementStrategies
# This is what we do when we see a cat. We currently only do a random 
# laser movement
class CatStrategy():
	# @laserGPIO: Singleton laser object with a connection to our laser
	# @motor: Singleton object with connection to our top servo and bottom
	# 		  servo of the pan-tilt
	def __init__(self,motors,laserGPIO):
		self.__LaserMovementStrategies = LaserMovementStrategies(laserGPIO,motors)
		

	def run(self):
		self.__LaserMovementStrategies.on()
		pass

