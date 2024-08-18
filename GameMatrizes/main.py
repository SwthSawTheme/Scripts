import keyboard
import os
from time import sleep

def matrizes():
    linhas = 25
    colunas = 35

    matriz = []

    for l in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(".")
        matriz.append(linha)
    return matriz

tela = matrizes()

def draw():    
    for linha in tela:
        print(" ".join(linha))

def main():

    # Posição do personagem
    x = len(tela) // 2
    y = len(tela) // 2

    while True:
        
        # preenche a matriz com o ultimo ponto
        tela[x][y] = "."

        if keyboard.is_pressed("a"):
            y -= 1
        
        if keyboard.is_pressed("d"):
            y += 1
        
        if keyboard.is_pressed("w"):
            x -= 1
        
        if keyboard.is_pressed("s"):
            x += 1

        # desenhar "Player"
        tela[x][y] = "0"
        
        os.system("cls")
        draw()
        sleep(0.03)
main()