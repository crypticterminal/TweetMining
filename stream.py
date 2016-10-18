import tweepy
import os
from datetime import datetime
import json
import pymongo
from mongo import mongo
import textblob
from show_feed import show_feed
from help_stream import help_stream


key=[]
max=100;

from twitter_authenticate import *

class StreamL(tweepy.StreamListener):
	counter=0
	def __init__(self,max_tweets=20000,*args,**kwargs):
		self.max_tweets = max_tweets
		self.counter = 0
		super(StreamL,self).__init__(*args, **kwargs)

	def on_connect(self):
		self.counter=0
		self.start_time=datetime.now()
		

	def on_data(self,data):
		if self.counter<=self.max_tweets:
			mongo()
			tweet=json.loads(data)
			tweets.insert(tweet)
			self.counter +=1
		else:
			tweetStream.disconnect()
			print("Max Limit Reached: Disconnecting.........")
			


	def on_error(self,status):
		print status


streamListen=StreamL(max_tweets=20000)
tweetStream=tweepy.Stream(authenticate,streamListen)





def stream():
	global max
	while(1):
		usr_inp=raw_input(">>>stream>>>")
		
		if usr_inp=="back":
			return

		elif usr_inp=="clear":
			os.system("clear")
			stream()

		elif usr_inp=="quit" or usr_inp=="exit":
			quit()
		
		elif usr_inp=="set_limit":
			max=raw_input("stream>>>set_max>>>")
		
		elif usr_inp=="show_limit":
			print("Limit: "+ str(max))

		elif usr_inp=="analyse" or usr_inp=="analyze":
			print("Not yet Implemented")

		elif usr_inp=="help":
			help_stream()

		elif usr_inp=="set_key":

			while(1):

				usr_inp=raw_input(">>>stream/set_key>>>")

				if usr_inp=="back":
					break

				elif usr_inp=="":
					usr_inp=raw_input(">>>stream/set_key")

				elif usr_inp=="show":
					for i in key:
						print i

				else:
					key.append(usr_inp)

		elif usr_inp=="show":
			for i in key:
				print i	
	
		elif usr_inp=="get_feed":
			tweetStream.filter(track=key)
		
		elif usr_inp=="show_feed":
			show_feed()			
	
		elif usr_inp=="analyse":
			print("analyse")
		
		elif usr_inp=="":
			usr_inp=raw_input(">>>stream>>>")	

		else:
			print("tweet_stream_analysis: "+usr_inp + " :command not recognised")
