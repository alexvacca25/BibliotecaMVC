
from models.material import Material

inventario=[]

def agregar_articulo(titulo,autor,tipo,anno_publica):
    articulo=Material(len(inventario)+1,titulo,autor,tipo,anno_publica)
    inventario.append(articulo)

def listar_articulos():
    return inventario