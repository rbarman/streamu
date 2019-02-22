import streamlink
import cv2

def get_stream(url, quality='best'):
	streams = streamlink.streams(url)
	if streams:
		return streams[quality].to_url()
	else:
		raise ValueError("No steams were available")

def display_stream(stream):
	cap = cv2.VideoCapture(stream)
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

if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser(description='Analyze streaming video')
	parser.add_argument('url',help="url of stream")
	args = parser.parse_args()

	stream = get_stream(args.url)
	display_stream(stream)
