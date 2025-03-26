from flask import Blueprint, render_template, request, flash
from Db.database import *
import sqlite3

user = Blueprint('user',__name__)

@user.route("/")
def home():
    return render_template("index.html")

@user.route("/registro", methods=["GET","POST"])
def Usuario():
    if request.method == "POST":
        user = request.form["campo1"]
        senha = request.form["campo2"]

        command, param = addUser(user,senha)
        try:
            db = sqlite3.connect("Navigator.db")
            cursor = db.cursor()
            cursor.execute(table_user)
            # Verificar se o usuário já existe
            cursor.execute("SELECT * FROM Usuario WHERE Username = ?", (user,))
            existing_user = cursor.fetchone()
            
            if existing_user:
                flash("Usuário já existe! Escolha outro nome.", "warning")
                print(f"Usuário {user} já existe!")
            else:
                # Criar usuário se não existir
                command, param = addUser(user, senha)
                cursor.execute(command, param)
                db.commit()
                flash("Usuário registrado com sucesso!", "success")
                print(f"Usuário {user} registrado com sucesso!")
        except Exception as e:
            print(f"Error:{e}")
        finally:
            if db:
                db.close()
                print("Conexão fechada com exito!")
    return render_template("user.html")