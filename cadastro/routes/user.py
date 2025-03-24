from flask import Blueprint, render_template, request

user = Blueprint('user',__name__)

@user.route("/")
def home():
    return render_template("user.html")

@user.route("/registro", methods=["POST"])
def Usuario():
    user = request.form["campo1"]
    senha = request.form["campo2"]