import os
import time

def shutdown(tempo=30):
    with open("out.bat","w") as file:
        data = file.write(f"shutdown /s /t {int(tempo)}")
        return data

if __name__ == "__main__":
    os.system("cls")
    os.system("title O Gato Preto")
    print("--Developer by Swth Saw Theme (._.)\n\n")
    try:
        shutdown()
        os.system("out.bat")
        os.system("cls")
        os.system("echo Desligando em 30 segundos...")
        time.sleep(3)
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        time.sleep(1)
        try:
            os.remove("out.bat")
        except PermissionError:
            print("Acesso Negado, Arquivo não pode ser excluido!")
