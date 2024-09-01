import json

# Teste simples de CRUD, Create, Read, Update e Delete

# Uso de funções encadeadas e manipulações de arquivos json



# Função responsavel por criar um arquivo json, nome a defini. Caso ele exista retorna um erro "FileExistsError"

def newFile(file:str):
    try:
        with open(f"{file}.json","x") as file:
            json.dump({},file,indent=4)

    except FileExistsError:
        return print("Arquivo já existe!")

# Função responsavel por ler o arquivo json, recebe como paramêtro o nome do arquivo já existente!

def readFile(file):
    try:
        with open(f"{file}.json", "r") as f:
            data = json.load(f)
            return data
        
    except FileNotFoundError:
        return print("Arquivo não existe!")

# Função responsavel por adicionar dados a o arquivo json

def writeFile(file,key,value):
    try:
        data = readFile(file)
        if data is None:
            return
        data[key] = value
        with open(f"{file}.json","w") as f:
            json.dump(data,f,indent=4)
            return "Gravado com sucesso!"
    except FileNotFoundError:
        return print("Arquivo não existe!")

# Função responsavel por excluir dados do arquivo json


# Controle do fluxo das funções

if __name__ == "__main__":
    while True:
        opcoes = ["1.Gravar","2.ler","3.Sair"]
        for item in opcoes:
            print(item)
        choice = int(input())
        if choice == 1:
            file = input("Digite o nome de um arquivo para gravar: ")
            key = input("Digite o nome de uma chave: ")
            value = input("Digite o nome de um valor para a chave: ")
            writeFile(file,key,value)
        elif choice == 2:
            dado = input("Digite o nome do arquivo para ler: ")
            file = readFile(dado)
            print(file)
        elif choice == 3:
            break