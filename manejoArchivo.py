from scrapLink import tomaLink
from scrapDescription import search

linkMaster='https://carros.mercadolibre.com.co/_Desde_'

def buscarLinks():
    archivo= open('linkML.txt','w')
    for escr in tomaLink():
        archivo.write(escr+'\n')

    archivo.close()
    print('listo los links')

def llenarInfo():
    archivo= open('holaaaaaa.txt','r')
    description=[]
    for leer in archivo:
        description.append(search(leer))
    archivo.close()
    
    archivo2= open('comoestas.txt','w')
    for escr in description:
        print(escr)
        escr=str(escr)
        archivo2.write(escr+'\n')

    archivo2.close()
    print('listo los links')
    
    
llenarInfo()