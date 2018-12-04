import pygame
import os
import random
from pygame import mixer
# This is essentially a way for us to modulize the pygame mixer class.
# This allows us to play a random song from a directory, and check if
# the file given is valid.
class SoundBox():
	# @soundDir: this is the directory with noises/songs in it for the
	# 			 soundbox to play
	def __init__(self,soundDir):
		__tunes = []
		self.__soundDir = soundDir
		mixer.init()
		if(os.path.isdir(soundDir)):
			self.__tunes = [file for file in os.listdir(soundDir)]
		else:
			raise Exception("The directory of the sounds file is not a valid directory.")
			
	# play a random song from the input directory of noises/songs
	def play(self):
		if(self.__tunes==[]):
			return
		# we give it a 50 percent chance to play the noise/song
		if(random.randint(0,1)==0):
			myTune = self.__soundDir+"/"+self.__tunes[random.randint(0,len(self.__tunes)-1)]
			print(myTune)
			mixer.music.load(myTune)
			mixer.music.play()
	# play a specific file from the directory we loaded at the beginning
	def playSpecificFile(self,someFile):
		if(os.path.isfile(self.__soundDir+"/"+someFile)):
			mixer.music.load(self.__soundDir+"/"+someFile)
			mixer.music.play()
