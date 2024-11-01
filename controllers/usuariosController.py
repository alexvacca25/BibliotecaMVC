from models.usuario import Usuario

usuarios=[]

def agregar_usuarios(nombre,email):
    usuario=Usuario(len(usuarios)+1,nombre,email)
    usuarios.append(usuario)

def listar_usuarios():
    return usuarios