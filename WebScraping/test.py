from datetime import datetime


data = datetime.now()

try:
    name = int(input(""))
    if len(name) == 3:
        print("Opa")

except Exception as e:
    contador = 0
    erro = f"\n{contador+1} Data: {data} | Erro: {e}"
    
    with open("logs.txt","a") as arquivo:
        arquivo.write(str(erro))
    

finally:
    print("Deu certo")