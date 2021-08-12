# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 03:18:08 2021

@author: snakk
"""


import requests
import json
import pandas as pd 
import time
from bs4 import BeautifulSoup as bs
import re
import os


base_url= "https://www.observerbd.com/"

def makesoup(url):
    doc= requests.get(url)
    
    if str(doc)=="<Response [200]>":
        soup= bs(doc.content, 'html.parser')
        print(f'received url:{url}')
    else:
        print(f"{url} cannot be reached.")
        
    return soup


def scrapeitall(urllist,start,end,sleep=3):
    dic=[]
    yr=2021   
    
    for url in urllist:
        for i in range(start,end+1):
            curr_url=url
            curr_url+=str(i)
            soup= makesoup(curr_url)
            
            for link in soup.find_all('div', class_="inner"):
                title=link.find("b").text
                scrapedurl=base_url+link.find("a").get('href')
                time.sleep(sleep)
                data= {"links":scrapedurl,"titles":title,"Year":yr}
                dic.append(data)
                time.sleep(sleep)
        yr-=1                      #Year count from 2021 to 2019 for each url loop
            
    df= pd.DataFrame(dic, dtype=str)
    return df

urllist=["https://www.observerbd.com/cat-adv.php?cd=1&key=accident&y=&pg=",             #Listed the urls for the search results of accident data for 2021,2020 and 2019 respectively
         "https://www.observerbd.com/cat-adv.php?cd=1&key=accident&y=2020&pg=",
         "https://www.observerbd.com/cat-adv.php?cd=1&key=road%20accident&y=2019&pg="]

datascraped= scrapeitall(urllist=urllist,start=1,end=26,sleep=1)  #You can set the sleep time=0 if your scraping is slow
path=r"E:\Machine Learning\Webscraping"         #Path for my local machine to create the csv output
datascraped.to_csv(os.path.join(path,'RoadAccidentsTheDailyObserver.csv'))




