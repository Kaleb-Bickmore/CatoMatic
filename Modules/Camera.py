class Camera():
	def __init__(self,piCamera):
		piCamera.resolution = (304,304)
		piCamera.framerate =32                                        
		self.__piCamera = piCamera
		self.__rawCapture =PiRGBArray(piCamera,size=(304,304))
	def captureContinousFeed(self):
		return __piCamera.capture_continuous(self.__rawCapture,format = "bgr",
		use_video_port=True)
	def captureOneImage(self):
		self.__piCamera.capture(self.__rawCapture, format="bgr")
		return self.__rawCapture.array
	def truncate(self):
		self.__rawCapture.truncate(0)
