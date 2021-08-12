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
df= df.iloc[:,1:4]   #Removing the indexes from the dataframe
url_links= df['links']
news=[]

#Running loop for each of the link of search results for 2021,2020 and 2019 respectively
for link in url_links:
    #making soup object from the link
    soup= makesoup(link)
    
    #Scraping the paragraph part only, where the news report body is present
    text=soup.findAll('p')[0].text
    
    #Using regular expressions to clear the beginning and ending whitespaces and newlines in between the paragraphs .Have to use + after ^\s because without + it will
    text= re.sub(r'(^\s+)|\n+', '', text)   # remove only one single whitespace. So the above line basically removes all the starting whitespaces and new lines
    
    #Appending the text to the news list, for making it a pd.Series later
    news.append(text)                       
    
df["News"]=news

path=r"E:\Machine Learning\Webscraping"
#print(df)
df.to_csv(os.path.join(path,'RoadAccidentsTheDailyObserver_encoding_corrected.csv'),index=False, encoding= 'utf-8-sig')
    
