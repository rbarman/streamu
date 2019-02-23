import streamlink
import cv2
import youtube_dl

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
	# TODO: add error catching
	info_dict = ydl.extract_info(url, download=False)
	req = info_dict.get('requested_formats')
	# TODO: req[0] has a fps feature -> send to display_capture which currently assumes 30 fps
	url = req[0].get('url')
	return url

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
					TODO: fix slow performance on live streaming video
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
