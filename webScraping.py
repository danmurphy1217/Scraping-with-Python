# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 21:14:48 2019

@author: Dan Murphy
Web Scraping Practice
"""
import requests
from bs4 import BeautifulSoup
from astropy.table import Table, Column
import numpy as np


url = "http://yann.lecun.com/exdb/mnist/"
response = requests.get(url)
print(response) # Check for 200 response
bs = BeautifulSoup(response.text, "html.parser")
aTags = bs.findAll('a') # Find all a tags


# loop through a tags and keep count of them
i = 1
for link in aTags:
    print("Here is link " + str(i) + ": " + str(link) +"\n")
    i+=1
# There are a total of 76 <a> tags on this page!

# Create a table to portray links
t = Table(names = ('Links', 'Description'))
print(t)

t.add_row(vals=(1, 2))
print(t)
# Messing aroudn with table values. More tomorrow...