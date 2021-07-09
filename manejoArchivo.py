from scrapLink import tomaLink
from scrapDescription import search

linkMaster='https://carros.mercadolibre.com.co/_Desde_'
#buscarLinks para buscar todos links de la url hasta que acabe
#buscarLinks()
#llenarInfo para leer los datos dentro del txt y llenar otro con los datos de cada enlace inicial
#precio, nombre, descripcion basica, url de imagen, url de videos
llenarInfo()
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
    
