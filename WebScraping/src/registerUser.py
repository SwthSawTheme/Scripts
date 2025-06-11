import sqlite3


def registerUser(name:str, level:str,title:str,data:str):
    insert = """
    INSERT INTO Usuarios (name, level, title, data)
    VALUES (?,?,?,?)
"""
    return insert, (name,level,title,data)

try:
    conexao = sqlite3.connect("AuroraHell.db")
    cursor = conexao.cursor()
    command, param = registerUser("Andre","999","Procurado Low", "06/06/06")
    cursor.execute(command,param)
    conexao.commit()
except Exception as e:
    print(f"Erro:{e}")
finally:
    if conexao:
        conexao.close()
        print("Conexão fechada com exito!")