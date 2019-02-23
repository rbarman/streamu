import argparse
from Display import display_webcam, display_livestream

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Analyze streaming video')
	parser.add_argument('-ls','-livestream',help='url of livestream',nargs=1)
	parser.add_argument('-w', action='store_true',help='toggle to display webcam')

	args = parser.parse_args()
	print(args)
	
	if args.w:
		display_webcam()
	if args.ls:
		display_livestream(args.ls[0])