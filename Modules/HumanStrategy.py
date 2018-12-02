from TopServo import TopServo
from BottomServo import BottomServo
from Laser import Laser
class HumanStrategy():
	def __init__(self,topServo,bottomServo,laserServo):
		self.__topServo = TopServo(topServo)
		self.__bottomServo = BottomServo(BottomServo)
		self.__laser = Laser(laserServo)

	def run(self):
		self.__laser.on()
		print("hooman, dance!")
		pass

