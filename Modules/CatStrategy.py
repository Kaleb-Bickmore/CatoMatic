from TopServo import TopServo
from BottomServo import BottomServo
from Laser import Laser
class CatStrategy():
	def __init__(self,topServo,bottomServo,laserServo):
		self.__topServo = TopServo(topServo)
		self.__bottomServo = BottomServo(BottomServo)
		self.__laser = Laser(laserServo)

	def run(self):
		print("laser for the kitty")
		self.__laser.on()
		pass

