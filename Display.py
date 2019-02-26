import streamlink
import youtube_dl
import cv2
from CascadeClassifier import CascadeClassifier

'''Methods related to displaying video via opencv'''

def display_livestream(url):
	'''Display an opencv VideoCapture from a streamlink supported livestream'''
	stream = get_livestream(url)
	cap = cv2.VideoCapture(stream)
	display_capture(cap)

def get_livestream(url, quality='best'):
	'''Get streaming url for streamlink supported stream'''
	streams = streamlink.streams(url)
	if streams:
		return streams[quality].to_url()
	else:
		raise ValueError("No steams were available")

def display_video(url):
	'''Display an opecv VideoCapture from a youtubedl supported video'''
	video = get_video(url)
	cap = cv2.VideoCapture(video)
	display_capture(cap)

def get_video(url):
	'''Get streaming url for a youtubedl supported video'''
	ydl = youtube_dl.YoutubeDL({})
	info_dict = ydl.extract_info(url, download=False)
	# youtube videos have different metadata
	if info_dict.get('extractor') == 'youtube':
		req = info_dict.get('requested_formats')
		# req also has fps feature
		return req[0].get('url')
	else:
		return info_dict.get('url')

def display_webcam():
	'''Display an opecv VideoCapture from webcam'''
	cap = cv2.VideoCapture(0)
	display_capture(cap)

def display_capture(cap):
	'''Display an opencv VideoCapture with face detection'''
	
	face_detector = CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

	# TODO: dynamically set frame rate
	frame_time = int((1.0 / 30.0) * 1000.0)
	
	while True:
		try:
			ret, frame = cap.read()
			if ret:
				# TODO: fix slow performance on live streaming video
				frame = face_detector.detect(frame)
				cv2.imshow('frame', frame)
				if cv2.waitKey(frame_time) & 0xFF == ord('q'):
					break
			else:
				break
		except KeyboardInterrupt:
			break

	cv2.destroyAllWindows()
	cap.release()
