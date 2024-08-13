from keyboard import is_pressed
from os import system
from time import sleep

linhas = 30
colunas = 50

matriz = []

for l in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(".")
    matriz.append(linha)

for m in matriz:
    print(" ".join(m))

