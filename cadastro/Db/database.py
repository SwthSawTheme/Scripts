table_user = """
    CREATE TABLE IF NOT EXISTS Usuario (
    ID_Username INTEGER PRIMARY KEY AUTOINCREMENT,
    Username VARCHAR(18) NOT NULL,
    Password VARCHAR(24) NOT NULL
    )
"""

def addUser(user:str,senha:str):
    insert = """
    INSERT INTO Usuario (Username,Password)
    VALUES (?,?)
"""
    return insert, (user,senha)
