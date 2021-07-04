# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 10:22:58 2021

@author: snakk
"""

import requests
import json
import pandas as pd 
import time
from bs4 import BeautifulSoup as bs
import re
import os
from Dailyobserver_webscraping_beautiful_soup import makesoup   #Using the previous file as module to import the makesoup function

df= pd.read_csv(r"E:\Machine Learning\Webscraping\RoadAccidentsTheDailyObserver.csv")   #Local machine filepath of the previously output csv file
url_links= df['links']
news=[]
for link in url_links:          #Scraping the main news report body by looping through all the links
    soup= makesoup(link)
    text=soup.findAll('p')[0].text
    text= re.sub(r'\n','',text)
    news.append(text)
    
df["News"]=news

path=r"E:\Machine Learning\Webscraping"
#print(df)
df.to_csv(os.path.join(path,'RoadAccidentsTheDailyObserver_new.csv'))
    
