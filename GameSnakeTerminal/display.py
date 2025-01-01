
ALTURA = 25
LARGURA = 50
matriz = []

def display():

    for i in range(ALTURA):
        linha = []
        for j in range(LARGURA):
            linha.append(".")
        matriz.append(linha)
    return matriz

def draw():
    for linha in matriz:
        print(" ".join(linha))



