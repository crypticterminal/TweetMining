import pymongo
from textblob import TextBlob
import time

sentim=""
subob=""
def show_feed():
	while 1:
		client=pymongo.MongoClient()
		db=client['db']
		tweets=db['tweets']

		it=tweets.find()

		for i in it:
				try:
					global sentim
					global subob
					sent=TextBlob(i['text'])
					(senti,subob)=sent.sentiment

					if subob<=0.5:
						subobr="Objective Statement"

					else:
						subobr="Subjective Statement"


					if senti<=(-0.1):
						sentim="Negative Sentiment"

					elif senti>(-0.1) and senti<=0.1:
						sentim="Neutral Sentiment"

					else:
						setim="Positive Sentiment"


			
					print("\n\n")
					print("Tweet::")
					print i['text']
					print("Screen Name: " +i['user']['screen_name'])
					print("User Name: " + i['user']['name'])
					print("Created on: " + i['created_at'])
					print("language: " + i['lang'])
					print("Sentiment: " + sentim) 
					print("Subjective/Objective: " + subobr)
				
				except:
					continue
