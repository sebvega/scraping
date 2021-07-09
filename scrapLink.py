from bs4 import  BeautifulSoup
import requests
import pandas as pd



def tomaLink():
    linkMaster='https://carros.mercadolibre.com.co/_Desde_'
    urls=[]
    count=1
    suma=0
    resultados=True

    while resultados:
        linkResultados=linkMaster+str(((48*(count-1))+(count-1)))
        page=requests.get(linkResultados)
        soup=BeautifulSoup(page.content, 'html.parser')
        elementSearch=soup.find_all('a', class_='andes-pagination__link ui-search-link')

        resultados=str(elementSearch)
        if linkResultados!='https://carros.mercadolibre.com.co/_Desde_0':
            resultados=resultados[resultados.find('https:'):] 
            resultados=resultados[resultados.find('\"'):]
        
        resultados=resultados[resultados.find('https:'):] 
        resultados=resultados[:resultados.find('\"')]
        iterator= ((48*(count-1))+(count-1))################
        link= linkMaster + str(iterator)
        page=requests.get(link)
        soup=BeautifulSoup(page.content, 'html.parser')
        elementSearch=soup.find_all('a', class_='ui-search-result__content ui-search-link')

        sub1='https:'
        sub2='\"'
        
        for enlace in elementSearch:
            enlace=str(enlace)
            index1=enlace.find(sub1)
            enlace=enlace[index1:]
            index2=enlace.find(sub2)
            url=enlace[:index2]
            urls.append(url)
        count+=1

    return urls









