import pygame
import os
import random
from pygame import mixer
class SoundBox():
	def __init__(self,soundDir):
		__tunes = []
		self.__soundDir = soundDir
		mixer.init()
		if(os.path.isdir(soundDir)):
			self.__tunes = [file for file in os.listdir(soundDir)]
		else:
			raise Exception("The directory of the sounds file is not a valid directory.")
			
	def play(self):
		
		if(self.__tunes==[]):
			return
		if(random.randint(0,1)==0):
			myTune = self.__soundDir+"/"+self.__tunes[random.randint(0,len(self.__tunes)-1)]
			print(myTune)
			mixer.music.load(myTune)
			mixer.music.play()
		
	def playSpecificFile(self,someFile):
		if(os.path.isfile(self.__soundDir+"/"+someFile)):
			mixer.music.load(self.__soundDir+"/"+someFile)
			mixer.music.play()
