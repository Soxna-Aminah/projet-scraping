
from model.modele import *
from expat import *
from jumia import *

def formatdata(lidata):
    for i in lidata:
        titre=i["libelle"].upper()
        if "CHAISE" in titre:
            i["categorie"]="chaise"
        elif "TABLE" in titre:
            i["categorie"]="table"
        else:
            i["categorie"]="autre"
    return lidata

jumia=formatdata(mydata)
expat=formatdata(lidata)
pagejumia=Pages("jumia","https://www.jumia.sn/")
pagexpat=Pages("Expat","https://www.expat-dakar.com/")
pagecoinafrique=Pages("Coin Afrique","https://www.coinafrique.com/")

def remplirdata(data,page):
    for j in data:
        cat=j["categorie"]
        lib=j["libelle"]
        img=j["img"]
        prix=j["price"]
        insertdata=Meubles(cat,lib,img,prix,page)

remplirdata(jumia,"jumia")
remplirdata(expat,"Expat")