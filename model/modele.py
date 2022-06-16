from sqlalchemy import *
from sqlalchemy.orm import * 
from sqlalchemy.ext.declarative import declarative_base
import sys
sys.path.append("..")




########################Engine########################

engine=create_engine('postgresql://scrap:passer123@localhost:5432/scraping')
base_session=sessionmaker(bind=engine,autocommit=False,autoflush=False)
session=base_session()
base=declarative_base()


class Pages(base):
    __tablename__='page'
    id_page=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(100))
    url=Column(String(500))
    meubles=relationship("Meubles")

    def __init__(self,name,url):
        self.name=name
        self.url=url
        session.add(self)
        session.commit()

###################### Meubles########################

class Meubles(base):
    __tablename__='meubles'
    id_meuble=Column(Integer,primary_key=True,autoincrement=True)
    categorie=Column(String(500))
    libelle=Column(String(00))
    image=Column(String(500))
    prix=Column(String(500))
    pageid=Column(Integer,ForeignKey('page.id_page'))

    def __init__(self,categorie,lib,img,prix,page):
            self.categorie=categorie
            self.libelle=lib
            self.image=img
            self.prix=prix
            self.pageid=session.query(Pages).filter(Pages.name==page).first().id_page
            session.add(self)
            session.commit()

def init_base():
    base.metadata.create_all(bind=engine)
init_base()

def recupmeubles():
    datameubles=session.query(Meubles.categorie,Meubles.libelle,Meubles.image,Meubles.prix,Pages.name).filter(Meubles.pageid==Pages.id_page).all()
    ndata=[]   
    for i in datameubles:
        if int(i["prix"])<=450:
            pass
        else:
            ndata.append(dict(i))

    return ndata



    
            







