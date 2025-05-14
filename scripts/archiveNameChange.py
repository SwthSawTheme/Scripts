import os


os.chdir("C:")
os.chdir(r"C:\Users\Saw\Pictures\archer")

diretorio = os.listdir()
count = 0
for i in diretorio:
    arq, ext = os.path.splitext(i)
    arquivo = os.path.join(os.getcwd(),i)
    destino = os.path.join(os.getcwd(),f"image.{count}{ext}")

    os.rename(arquivo,destino)
    count += 1

diretorio = os.listdir()
print(diretorio)