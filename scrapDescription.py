from bs4 import  BeautifulSoup
import requests
import pandas as pd




def listar(elemento):
    salida=list()
    for i in elemento:
        salida.append(i.text)
    return salida

def search(link):
    
    page=requests.get(link)
    soup=BeautifulSoup(page.content, 'html.parser')
    descPrice=soup.find_all('span', class_='price-tag-fraction')
    descPrice=listar(descPrice)
    descName=soup.find_all('h1', class_='ui-pdp-title')
    descName=listar(descName)
    principal=soup.find_all('th', class_='andes-table__header andes-table__header--left ui-pdp-specs__table__column ui-pdp-specs__table__column-title')
    principal=listar(principal)
    notes=soup.find_all('span', class_='andes-table__column--value')
    notes=listar(notes)
    totalDescription={'descName':descName,'descPrice':descPrice}
    
    descTittle=soup.find_all('h2', class_='ui-pdp-description__title')
    descTittle=listar(descTittle)
    descIndex=soup.find_all('p', class_='ui-pdp-description__content')
    descIndex=listar(descIndex)
    espec = dict(zip(principal, notes))
    espec1=dict(zip(descTittle,descIndex))
    
    totalDescription.update(espec)
    totalDescription.update(espec1)
    images=[]
    images2=[]
    images=pictures(link)
    max=len(images)
    for i in range(max):
        images2.append(i+1)
    espec2=dict(zip(images2,images))
    totalDescription.update(espec2)
    return totalDescription



def pictures(link):
    page=requests.get(link)
    soup=BeautifulSoup(page.content, 'html.parser')
    elementSearch=soup.find_all('figure', class_='ui-pdp-gallery__figure')
    sub1='https:'
    sub2='\"'
    urls=[]
    for enlace in elementSearch:
        enlace=str(enlace)
        index1=enlace.find(sub1)
        enlace=enlace[index1:]
        index2=enlace.find(sub2)
        url=enlace[:index2]
        urls.append(url)
    return urls



