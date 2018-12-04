from LaserMovementStrategies import LaserMovementStrategies
# This is what we do when we see a cat. We currently only do a random 
# laser movement
class CatStrategy():
	def __init__(self,motors,laserServo):
		self.__LaserMovementStrategies = LaserMovementStrategies(laserServo,motors)
		

	def run(self):
		self.__LaserMovementStrategies.on()
		pass

