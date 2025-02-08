matriz = []

coluna = 15
linha = 10

for i in range(coluna):
    linhas = []
    for j in range(linha):
        linhas.append(".")
    matriz.append(linhas)

for i in matriz:
    print(" ".join(i))
