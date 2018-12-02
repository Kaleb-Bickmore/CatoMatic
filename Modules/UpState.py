class UpState():
	def __init__(self,topServo):
		self.__topServo = topServo
	def move(self):
		self.__topServo.min()
	def moveMiddle(self):
		self.__topServo.mid()
