import requests
import json
import pandas as pd 
import time
from bs4 import BeautifulSoup as bs 
from make_soup import*


def links_headlines_dates(soup):
    container = soup.find("div",attrs = {"class":"content-blocks"})
    item = container.find_all('div', attrs = {"class": "news-block-four"})
    links = []
    headlines = []
    dates = []
    for i in range(len(item)):
        date = item[i].find("li")
        title = item[i].find("h3", attrs = {"class" : "h3-edit"})
        dates.append(date.text)
        headlines.append(title.text)
        link = item[i].find('a')
        if 'href' in link.attrs:
            links.append(link.attrs['href'])
    return links , headlines , dates