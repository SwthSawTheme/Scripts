import sqlite3

table_user = """
    CREATE TABLE IF NOT EXISTS Usuario (
    ID_Usuario INTERGER PRIMARY KEY AUTOINCREMENT,
    Usuario VARCHAR(18) NOT NULL,
    Senha VARCHAR(24) NOT NUL
    )
"""

def addUser(user:str,senha:str):
    insert = """
    INSERT INTO Usuario (user,senha)
    VALUES (?,?)
"""
    return insert, (user,senha)

try:
    db = sqlite3.connect("Navigator.db")
    cursor = db.cursor()
    insert,parametros = addUser()