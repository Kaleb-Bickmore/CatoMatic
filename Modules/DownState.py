# This represents our motors in a down looking state
class DownState():
	def __init__(self,topServo):
		self.__topServo = topServo
	def move(self):
		self.__topServo.max()
	def moveMiddle(self):
		self.__topServo.mid()
