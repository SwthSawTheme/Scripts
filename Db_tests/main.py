import sqlite3 as sql


table = """
    CREATE TABLE IF NOT EXISTS USER (
    ID_User INTEGER PRIMARY KEY AUTOINCREMENT,
    Character VARCHAR(50) NOT NULL,
    Level INTERGER NOT NULL
    )
"""

def addUser(character: str, level:int):
    insert = """
    INSERT INTO USER (Character, level)
    VALUES (?,?)
"""
    return insert, (character,level)


while True:
    char = str(input("Nome do personagem: "))
    level = int(input("Level: "))

    try:
        conexao = sql.connect("Database.db")
        cursor = conexao.cursor()
        command, params = addUser(char,level)
        cursor.execute(table)
        cursor.execute(command,params)
        conexao.commit()
        print("Banco de dados atualizado!")
    except Exception as e:
        print(f"Erro {e}")
    finally:
        if conexao:
            conexao.close()
            print("Conexão finalizada com o banco de Dados")