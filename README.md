# TweetMining   [![Build Status](https://travis-ci.org/vduddu/TweetMining.svg?branch=master)](https://travis-ci.org/vduddu/TweetMining) [![NSP Status](https://nodesecurity.io/orgs/vduddu/projects/efc25a8b-2bd8-441f-ac0e-1d0e16be5e3c/badge)](https://nodesecurity.io/orgs/vduddu/projects/efc25a8b-2bd8-441f-ac0e-1d0e16be5e3c)
TweetMining is a command line tool to get live tweets based on user input keywords and performs sentiment analysis on these tweets. It uses Twitter's streaming API to get all the tweets corrresponding to the keywords and stores them in mongo database.
TextBlob library is used to perform sentiment analysis on these tweets.

## Getting Started

### Requirements

Textblob
    
    pip install textblob
    
Tweepy
    
    pip install tweepy
  
Pymongo
    
    pip install pymongo
    
PyFiglet

    pip install pyfiglet
 
### Executing the tool

    python main.py
 
## ScreeenShots


### Startup Screen

![screen shot 2016-11-09 at 7 48 14 pm](https://cloud.githubusercontent.com/assets/20644368/20141258/87cf6572-a6b5-11e6-8935-f323e1696bc9.png)

#### List of all the stream commands

![screen shot 2016-10-17 at 5 52 31 pm](https://cloud.githubusercontent.com/assets/20644368/19441152/3def8d9e-94a2-11e6-966c-6442670acbff.png)


#### The output of show_feed command

![screen shot 2016-10-17 at 5 34 08 pm](https://cloud.githubusercontent.com/assets/20644368/19441113/1bf4a90e-94a2-11e6-9100-26b2e0756221.png)

## Developer
Vasisht Duddu(vduddu)

## License
This project is licensed under the MIT License - see the LICENSE file for details
