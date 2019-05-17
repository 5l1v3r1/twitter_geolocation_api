#!/usr/bin/env python 

import tweepy 
from mystreamlistener import MyStreamListener

access_token = "**********************************************" 
access_token_secret = "*****************************************" 
consumer_key = "************************************************" 
consumer_secret = "********************************************" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 

l = MyStreamListener() 
stream = tweepy.Stream(auth, l) 
stream.filter(track=['#Acte25', '#GiletJaune']) 



  

