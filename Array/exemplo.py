from keyboard import is_pressed
import os
from time import sleep

# Definindo dimensões da matriz
linhas = 30
colunas = 50

# Inicializando a matriz
matriz = [["." for _ in range(colunas)] for _ in range(linhas)]

# Inicializando a posição do número 1
x, y = linhas // 2, colunas // 2
matriz[x][y] = "1"

def print_matriz():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal
    for linha in matriz:
        print(" ".join(linha))

def mover(ant_x, ant_y, nova_x, nova_y):
    matriz[ant_x][ant_y] = "."
    matriz[nova_x][nova_y] = "1"

# Loop principal
while True:
    # Desenha a matriz
    print_matriz()
    sleep(0.03)

    # Movendo o número 1 baseado na entrada do teclado
    if is_pressed('a') and y > 0:
        mover(x, y, x, y - 1)
        y -= 1
    elif is_pressed('d') and y < colunas - 1:
        mover(x, y, x, y + 1)
        y += 1
    elif is_pressed('w') and x > 0:
        mover(x, y, x - 1, y)
        x -= 1
    elif is_pressed('s') and x < linhas - 1:
        mover(x, y, x + 1, y)
        x += 1