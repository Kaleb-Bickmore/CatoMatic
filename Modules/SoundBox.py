import pygame
import os
import random
Class SoundBox():
	def __init__(self,soundsFile):
		__tunes = []
		if(os.path_isdir(soundsFile):
			self.__tunes = [file for file in os.listdir(soundsFile)]
		else:
			raise Exception("The directory of the sounds file is not a valid directory.")
			
	def play(self):
		if(self.__tunes==[]):
			return
		pygame.mixer.load(self.__tunes[random.randint(0,len(self.__tunes)-1)])
		pygame.mixer.play()
		
	def playSpecificFile(self,someFile):
		if(os.path_isfile(someFile)):
			pygame.mixer.load(someFile)
			pygame.mixer.play()
