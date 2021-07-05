# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 05:12:32 2021

@author: snakk
"""

import pandas as pd 
import re

df= pd.read_csv(r"E:\Machine Learning\Webscraping\RoadAccidentsTheDailyObserver_regex.csv")



#df["bool"]= [(df["titles"][i] in df["News"][i]) for i in range(df.shape[0])]
#df["replaced"]=[(df["News"][i].replace(df["titles"][i],"")) for i in range(df.shape[0])]

# =============================================================================
# #Removing the headline/title from the newsbody first, because of the improper punctuation and lack of whitespace
# 
# def getit(row):
#  try:
#   return row.News.replace(row.titles,"")
#  except:
#   return row.News # in case row.get("titles") return non-string
# 
# df["replaced"] = df.apply(getit , axis = 1)
# 
# df= df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
# 
# 
# #Adding the headline to the news body with a colon................
# df["cleaned"]= df.titles+": "+df.replaced
# =============================================================================

#First, let's strip off the beginning and ending whitespaces from the whole
#dataframe if the entries are string===========================================

df= df.applymap(lambda x: x.strip() if isinstance(x, str) else x)   #.apply() is for a single pd series while .applymap() applies for the whole dataframe

#Now, let's use apply method to replace the headlines that are already on the Newsbody
#with proper punctuation ": " and those news which do not have title in the body, add
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

