#!/usr/bin/env python 

import tweepy 
from mystreamlistener import MyStreamListener

access_token = "714603694231261184-VKQ8vCD1SydRQczSQbOcVJ7rAOGELpA" 
access_token_secret = "lbtHEPxTsPLz7biD3zXGK4qbKb1NnvOM1TTB5OCAcTyDW" 
consumer_key = "08MdWk1vyQPcuUDuKobOjy5l6" 
consumer_secret = "lKUiXzMS155BS6jJGRe225NznCgrXth8to0LP8jN6YGaT9glXY" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 

l = MyStreamListener() 
stream = tweepy.Stream(auth, l) 
stream.filter(track=['#Acte25', '#GiletJaune']) 



  

