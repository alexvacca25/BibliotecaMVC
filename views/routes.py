

from flask import Blueprint, redirect, render_template, request, url_for

from controllers.inventarioController import agregar_articulo, listar_articulos
from controllers.reservasController import prestamo_material
from controllers.usuariosController import agregar_usuarios, listar_usuarios


app=Blueprint('app',__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inventario")
def listar_inventario():
    lista_materiales=listar_articulos()
    return render_template("catalogo.html",materiales=lista_materiales)

@app.route('/add_material', methods=["POST"])
def ingresar_articulos():
    titulo=request.form["titulo"]
    autor=request.form["autor"]
    tipo=request.form["tipo"]
    anno=request.form["anno_publica"]

    agregar_articulo(titulo,autor,tipo,anno)
    return redirect(url_for("app.listar_inventario"))

@app.route("/usuarios", )
def usuarios():
    lista_usuarios=listar_usuarios()
    return render_template("usuarios.html",usuarios=lista_usuarios)

@app.route("/add_usuario", methods=["POST"])
def ingresar_usuario():
   nombre=request.form["nombre"]
   email=request.form["email"] 
   agregar_usuarios(nombre,email)
   return redirect(url_for("app.usuarios"))


@app.route("/reservas")
def reservas():
    lista_materiales=listar_articulos()
    lista_usuarios=listar_usuarios()
    return render_template("reservas.html",usuarios=lista_usuarios,materiales=lista_materiales)

@app.route("/prestamo_material", methods=["POST"])
def prestar_material():
    usuario_id=int(request.form["usuario_id"])
    material_id=int(request.form["material_id"])
    prestamo_material(usuario_id,material_id)
    return redirect(url_for("app.usuarios"))
