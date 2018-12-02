class RightState():
	def __init__(self,bottomServo):
		self.__bottomServo = bottomServo
	def move(self):
		self.__bottomServo.min()
	def moveMiddle(self):
		self.__bottomServo.mid()
