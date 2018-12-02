from Laser import Laser
from SoundBox import SoundBox
class HumanStrategy():
	def __init__(self,motors,laserServo):
		self.__motors = motors
		self.__laser = Laser(laserServo,motors)
		self.__soundBox = SoundBox("../R2Noises")
		
	def run(self):
		self.__soundBox.play()
		self.__laser.on()
		pass

