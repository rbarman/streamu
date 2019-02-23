import streamlink
import cv2

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
	frame_time = int((1.0 / 30.0) * 1000.0)

	while True:
		try:
			ret, frame = cap.read()
			if ret:
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