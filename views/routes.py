

from flask import Blueprint, redirect, render_template, request, url_for

from controllers.inventarioController import agregar_articulo, listar_articulos


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

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

@app.route("/add_usuario")
def ingresar_usuario():
    