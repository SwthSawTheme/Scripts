import sqlite3


table_user = """
    CREATE TABLE IF NOT EXISTS Usuarios (
    ID_User INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(25) NOT NULL,
    Level VARCHAR(6) NOT NULL,
    Title VARCHAR(25) NOT NULL,
    Data VARCHAR(25) NOT NULL)
"""

try:
    conexao = sqlite3.connect("AuroraHell.db")
    cursor = conexao.cursor()
    cursor.execute(table_user)
except Exception as e:
    print(f"Erro:{e}")
finally:
    if conexao:
        conexao.close()
        print("Conexão fechada com exito!")