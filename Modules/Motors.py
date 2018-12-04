from RightState import RightState
from LeftState import LeftState
from UpState import UpState
from DownState import DownState
import random
	# This class is used to control our servos in a way that we
	# keep track of the state of our servos. We must do this,
	# otherwise we would move randomly.
class Motors():
	__possibleStates = {}
	def __init__(self,topServo,bottomServo):
		self.__possibleStates["up"] = UpState(topServo)
		self.__possibleStates["left"] = LeftState(bottomServo)
		self.__possibleStates["down"] = DownState(topServo)
		self.__possibleStates["right"] = RightState(bottomServo)
		self.__currentState =[]
		self.move(["down"])

	# @direction: array of new states to move to.
	# repositions our servos to center, then it moves to the new states
	# after it has been centered.
	def move(self,direction):
		self.moveMiddle()
		for newStates in direction:
			if(newStates in self.__possibleStates): 
				self.__possibleStates[newStates].move()
				self.__currentState.append(newStates)
			else:
				raise Exception(str(newStates) + " is not a valid position to move To")
		pass
	
	# uses the States in the current state to get back to center
	def moveMiddle(self):
		for states in self.__currentState:
			if(states in self.__possibleStates): 
				self.__possibleStates[states].moveMiddle()
			else:
				raise Exception(str(states) + " is not a valid position to move from")
		self.__currentState = []
		pass
	# Picks a random key from our possible moves and calls move with
	# the random key it picked
	def randomMove(self):
		possibleMoves = list(self.__possibleStates.keys())
		randomMove = [possibleMoves[random.randint(0,3)]]
		randomMove.append(possibleMoves[random.randint(0,3)])
		randomMove = list(set(randomMove))
		self.move(randomMove)
