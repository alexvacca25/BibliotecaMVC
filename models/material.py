

class Material:
    def __init__(self,id,titulo,autor,tipo,anno_publica):
        self.id=id
        self.titulo=titulo
        self.autor=autor
        self.tipo=tipo
        self.anno_publica=anno_publica

    def __repr__(self):
        return f"<Material {self.tipo} => Titulo: {self.titulo} Autor: {self.autor} Año: {self.anno_publica} >"