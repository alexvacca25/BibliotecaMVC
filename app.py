
from views.routes import app as routes_app
import os
import sqlite3

from flask import Flask


DATABASE="database.db"


def iniciar_db():
    if not os.path.exists(DATABASE):
        conn=sqlite3.connect(DATABASE)
        cursor=conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS materiales(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       titulo TEXT NOT NULL,
                       auto TEXT NOT NULL,
                       tipo TEXT NOT NULL,
                       anno_publica INTEGER NOT NULL
                       )
                       ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       email TEXT NOT NULL,
                       materiales_prestados TEXT
                       )

                ''' )
        conn.commit()
        conn.close()

def iniciar_app():
    app=Flask(__name__,template_folder="views/templates")
    app.config["DATABASE"]=DATABASE

    app.register_blueprint(routes_app)

    return app

if __name__=='__main__':
    iniciar_db()
    app=iniciar_app()
    app.run(debug=True)

    