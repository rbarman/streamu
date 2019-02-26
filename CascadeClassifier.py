import cv2

class CascadeClassifier:

	def __init__(self, haarcascade):
		self.haarcascade = haarcascade
		self.cascade = cv2.CascadeClassifier(haarcascade)

	def detect(self,image, scaleFactor = 1.1, minNeighbors = 3, box_color = (255,0,0)):
		''' Draw a box around the identified object
			Uses opencv https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html#aaf8181cb63968136476ec4204ffca498
		'''
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		matches = self.cascade.detectMultiScale(gray, scaleFactor, minNeighbors)
		for (x,y,w,h) in matches:
			cv2.rectangle(image,(x,y),(x+w,y+h),box_color,5)
		return image