
class Usuario:
    def __init__(self, id, nombre, email, materiales_prestados=None):
        self.id=id
        self.nombre=nombre
        self.email=email
        self.materiales_prestados= materiales_prestados or []


    def __repr__(self):
        return f"<Usuario: {self.nombre} : {len(self.materiales_prestados)} Materiales>"
