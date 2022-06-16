import requests
from bs4 import BeautifulSoup
import re

def get_price(str1):
    li=(re.findall("\d+", str1))
    nbr=""
    for i in li:
        nbr+=i
    return nbr


url5="https://www.jumia.sn/catalog/?q=meubles+bureau&page=2#catalog-listing"
def recuppage(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    block=soup.find(class_="-paxs row _no-g _4cl-3cm-shs")
    article=list(block.find_all('article',class_="prd _fb col c-prd"))
    # print(article)
    lidata=[]
   
    for i in article:
        dicdat={}
        dicdat["img"]= i.find('img').get("data-src")
        dicdat["libelle"]=i.find(class_='name').get_text()
        dicdat["price"]=get_price(i.find(class_="prc").get_text())

        
        lidata.append(dicdat)
    return lidata
mydata=recuppage(url5)



   
   