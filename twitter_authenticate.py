import tweepy

token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
token_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_key='XXXXXXXXXXXXXXXXXXXXXXXXXXX'  					#api_key
consumer_secret_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'   	#api_secret


try:
	authenticate=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
	authenticate.set_access_token(token,token_secret)
	print("User has been authenticated successfully")


except:
	print("There was some error in the authentication process")

