import streamlink
import cv2

'''Methods related to displaying video via opencv'''

def display_stream(url):
	'''Display an opencv VideoCapture from a streamlink supported stream'''
	stream = get_stream(url)
	cap = cv2.VideoCapture(stream)
	display_capture(cap)

def get_stream(url, quality='best'):
	'''Get streamlink supported stream from url'''
	streams = streamlink.streams(url)
	if streams:
		return streams[quality].to_url()
	else:
		raise ValueError("No steams were available")

def display_webcam():
	'''Display an opecv VideoCapture from webcam'''
	cap = cv2.VideoCapture(0)
	display_capture(cap)

def display_capture(cap):
	'''Display an opencv VideoCapture with face detection'''
	
	face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
	frame_time = int((1.0 / 30.0) * 1000.0)
	
	while True:
		try:
			ret, frame = cap.read()
			if ret:
				'''detect face on frame
					TODO: fix slow performance on streaming video
				'''
				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				faces = face_cascade.detectMultiScale(gray, 1.3, 5)
				for (x,y,w,h) in faces:
				    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)

				cv2.imshow('frame', frame)
				if cv2.waitKey(frame_time) & 0xFF == ord('q'):
					break
			else:
				break
		except KeyboardInterrupt:
			break

	cv2.destroyAllWindows()
	cap.release()
