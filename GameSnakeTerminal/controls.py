import keyboard
import os
import time
from display import *

tela = display()

def main():
    
    x = len(tela) // 2
    y = len(tela) // 2

    while True:
        tela[x][y] = "."

        if keyboard.is_pressed("a"):
            y -= 1
        elif keyboard.is_pressed("d"):
            y += 1
        elif keyboard.is_pressed("w"):
            x -= 1
        elif keyboard.is_pressed("s"):
            x += 1
        
        tela[x][y] = "#"

        os.system("cls")
        draw()
        time.sleep(0.05)