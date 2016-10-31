# TweetMining
TweetMining is a command line tool to get live tweets based on user input keywords and performs sentiment analysis on these tweets. It uses Twitter's streaming API to get all the tweets corrresponding to the keywords and stores them in mongo database.
TextBlob library is used to perform sentiment analysis on these tweets.

##Pre-Requirements

Textblob
    
    pip install textblob
    
Tweepy
    
    pip install tweepy
  
Pymongo
    
    pip install pymongo
    
PyFiglet

    pip install pyfiglet
 
##Executing the tool

    python main.py
 
##ScreeenShots


List of all the stream commands

![screen shot 2016-10-17 at 5 52 31 pm](https://cloud.githubusercontent.com/assets/20644368/19441152/3def8d9e-94a2-11e6-966c-6442670acbff.png)


The output of show_feed command

![screen shot 2016-10-17 at 5 34 08 pm](https://cloud.githubusercontent.com/assets/20644368/19441113/1bf4a90e-94a2-11e6-9100-26b2e0756221.png)

##Developer
vduddu

##License
This project is licensed under the MIT License - see the LICENSE file for details
