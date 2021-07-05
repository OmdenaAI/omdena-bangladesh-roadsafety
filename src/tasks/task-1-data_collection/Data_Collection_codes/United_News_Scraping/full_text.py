

import requests
import json
import pandas as pd 
import time
from bs4 import BeautifulSoup as bs 
from make_soup import*

def full_text(links):
    full_text = []
    for link in links:
        page_soup = make_soup(link)
        article =''
        paragraph_list = page_soup.find_all('p')
        for i in range(len(paragraph_list)):
            if paragraph_list[i].find('a'):
                pass
            else:
                article = article+paragraph_list[i].text
        full_text.append(article)
    return full_text
            

    