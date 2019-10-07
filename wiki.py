import html 
import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/Main_Page")
print(response) #check for successful request
bs = BeautifulSoup(response.text, "html.parser")
spanTags = bs.findAll('span')
num = 1
for tag in spanTags:
    print("This is tag " + str(num) + ":" + str(tag) + "\n")
    num += 1
