import requests
import json
import pandas as pd 
import time
from bs4 import BeautifulSoup as bs 
from make_soup import*

# putting it all together into a function
def make_soup(url):
    doc = requests.get(url)
    if str(doc) == "<Response [200]>":
        #create a soup object that contains have navigable html presentation of the page
        soup = bs(doc.content,'html.parser')
        print(f"Retrived url:{url}")
    else:
        print(f"{url} cannot be reached.")
    return soup