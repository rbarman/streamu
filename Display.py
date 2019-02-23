import streamlink
import cv2

import numpy as np
import cv2 as cv

'''Methods related to displaying video via opencv'''

def get_stream(url, quality='best'):
	streams = streamlink.streams(url)
	if streams:
		return streams[quality].to_url()
	else:
		raise ValueError("No steams were available")

def display_stream(url):
	stream = get_stream(url)
	cap = cv2.VideoCapture(stream)
	display_capture(cap)

def display_capture(cap):

	face_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
	frame_time = int((1.0 / 30.0) * 1000.0)
	
	while True:
		try:
			ret, frame = cap.read()
			if ret:
				'''detect face on frame
					TODO: fix slow performance on streaming video
				'''
				gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
				faces = face_cascade.detectMultiScale(gray, 1.3, 5)
				for (x,y,w,h) in faces:
				    cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)

				cv2.imshow('frame', frame)
				if cv2.waitKey(frame_time) & 0xFF == ord('q'):
					break
			else:
				break
		except KeyboardInterrupt:
			break

	cv2.destroyAllWindows()
	cap.release()

def display_webcam():
	cap = cv2.VideoCapture(0)
	display_capture(cap)