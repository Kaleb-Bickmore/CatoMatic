class LeftState():
	def __init__(self,bottomServo):
		self.__bottomServo = bottomServo
	def move(self):
		self.__bottomServo.max()
	def moveMiddle(self):
		self.__bottomServo.mid()
