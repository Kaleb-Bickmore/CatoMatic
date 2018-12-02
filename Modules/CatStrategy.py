from Laser import Laser
class CatStrategy():
	def __init__(self,motors,laserServo):
		self.__laser = Laser(laserServo,motors)

	def run(self):
		self.__laser.on()
		pass

