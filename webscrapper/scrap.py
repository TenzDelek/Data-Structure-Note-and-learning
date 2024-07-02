'''
install beautiful soup and requests
if a website doesnt have an api we normally scrap the data. but not all website 
are happy when we do it so be carefull
'''
import requests
from bs4 import BeautifulSoup

req=requests.get("https://monlam.ai/")
soup=BeautifulSoup(req.content,"html.parser")
ress=soup.title
# print(soup.prettify())
# print(soup.get_text())
print(ress.prettify())