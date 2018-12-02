from RightState import RightState
from LeftState import LeftState
from UpState import UpState
from DownState import DownState
class Motors():
	__possibleStates = {}
	def __init__(self,topServo,bottomServo):
		self.__possibleStates["up"] = UpState(topServo)
		self.__possibleStates["left"] = LeftState(bottomServo)
		self.__possibleStates["down"] = DownState(topServo)
		self.__possibleStates["right"] = RightState(bottomServo)
		self.__currentState =[]
		self.move(["down"])

	def move(self,direction):
		self.moveMiddle()
		for newStates in direction:
			if(newStates in self.__possibleStates): 
				self.__possibleStates[newStates].move()
				self.__currentState.append(newStates)
			else:
				raise Exception(str(newStates) + " is not a valid position to move To")
		pass
	
	def moveMiddle(self):
		for states in self.__currentState:
			if(states in self.__possibleStates): 
				self.__possibleStates[states].moveMiddle()
			else:
				raise Exception(str(states) + " is not a valid position to move from")
		self.__currentState = []
		pass
