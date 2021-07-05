# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 05:12:32 2021

@author: snakk
"""

import pandas as pd 
import re

df= pd.read_csv(r"E:\Machine Learning\Webscraping\RoadAccidentsTheDailyObserver_encoding_corrected.csv") #This is where the .csv file was located in my local machine,
                                                                                                         #Drive link: https://docs.google.com/spreadsheets/d/1Esb-1DOV4PtajCx582nt1Z_F_-OwbwD7aWF-c165RgY/edit#gid=1705484839

#First, let's strip off the beginning and ending whitespaces from the whole dataframe if the entries are string===========================================

df= df.applymap(lambda x: x.strip() if isinstance(x, str) else x)   #.apply() is for a single pd series while .applymap() applies for the whole dataframe

#Now, let's use apply method to replace the headlines that are already on the Newsbody with proper punctuation ": " and those news which do not have title in the body, add
#the title to the body for those with a ": "

def addheadlines(row):
    if row.titles in row.News:
        try:
            return row.News.replace(row.titles,row.titles+": ")
        except:
            return row.News # in case row.get("titles") return non-string
        
    else:
        return row.titles+": "+row.News

df["combined"]= df.apply(addheadlines, axis="columns")

