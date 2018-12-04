from SoundBox import SoundBox
# This is what we do when we see a Human. We currently play a noise when
# We see a human
class HumanStrategy():
	def __init__(self):
		self.__soundBox = SoundBox("../R2Noises")
		
	def run(self):
		self.__soundBox.play()
		pass

