from tweepy import *
import textblob
from twitter_authenticate import *
import pymongo
from help import help
import os
from stream import * 
from datetime import datetime

def main():
	while(1):
		
		usr_inp=raw_input(">>>")

		if usr_inp=="":
			usr_inp=raw_input(">>>")

		elif usr_inp=="exit" or usr_inp=="quit":
			quit()

		elif usr_inp=="help":
			help()
 		
		elif usr_inp=="clear":
			os.system("clear")
			main()

		elif usr_inp=="stream":
			stream()	

		else:
			print("tweet_stream_analysis: "+usr_inp+" : command not recognised")
			main()

os.system("clear")
help()
main()
