import json


data = {
    "Nome": "joao",
    "Idade": 20,
    "Data-Nascimento": "22/02/1998"
}

try:
    with open("data.json", "x") as arquivo:
        json.dump(data,arquivo,indent=4)
except FileExistsError:
    with open("data.json","r") as arquivo:
        dado = json.load(arquivo)
        print(f"Conteudo do arquivo: {dado.keys()}")