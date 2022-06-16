import requests
from bs4 import BeautifulSoup
from jumia import get_price

url1="https://www.expat-dakar.com/mobilier-de-bureau?sdc_search_offer_id=se4u0lfmxp"
url2="https://www.expat-dakar.com/mobilier-de-bureau?sdc_search_offer_id=se4u0lfmxp&page=2"
url3="https://www.expat-dakar.com/mobilier-de-bureau?sdc_search_offer_id=gjvxwjeess&page=3"
url4="https://www.expat-dakar.com/mobilier-de-bureau?sdc_search_offer_id=gjvxwjeess&page=4"
url5="https://www.expat-dakar.com/mobilier-de-bureau?sdc_search_offer_id=gjvxwjeess&page=5"
url6="https://www.expat-dakar.com/mobilier-de-bureau?sdc_search_offer_id=gjvxwjeess&page=6"

def scrapexpat(url):
    
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    block=soup.find_all(class_="listings-cards__list-item")
    lidata=[]
    
    for i in block:
        data={}
        lib=i.find(class_="listing-card__header__title")
        img=i.find('img')
        price=i.find('span',class_="listing-card__price__value")
        
        # print(price)
        if price==None:
            pass
        
        else:
            data["price"]=get_price(price.get_text())
            data["libelle"]=lib.get_text()
            data["img"]=img.get('src')
            lidata.append(data)
    
    return lidata


lidata1 = scrapexpat(url1)
lidata2 = scrapexpat(url2)
lidata3 = scrapexpat(url3)
lidata4 = scrapexpat(url4)
lidata5 = scrapexpat(url5)
lidata6 = scrapexpat(url6)

lidata = lidata1+lidata2+lidata3+lidata4+lidata5+lidata6

print(lidata)


        




    
    