from LaserMovementStrategies import LaserMovementStrategies
# This is what we do when we see a Dog. We currently only do a random 
# laser movement
class DogStrategy():
	def __init__(self,motors,laserServo):
		self.__LaserMovementStrategies = LaserMovementStrategies(laserServo,motors)
	def run(self):
		self.__LaserMovementStrategies.on()
		pass
