import keyboard
from time import sleep
from os import system

def main():
    vida = 100
    hit = 0

    try:
        while True:
            print(f"Vida: {vida}\nHit: {hit}")
            print("\nPara hitar pressione (espaço)\nPara incrementar o dano, pressione (w)\nPara decrementar o dano, pressione (s)\nPara restaurar a vida, pressione (h)")
            
            if keyboard.is_pressed('space'):
                vida -= hit

            elif keyboard.is_pressed('w'):
                hit += 10
        
            elif keyboard.is_pressed('s'):
                hit -= 10

            if keyboard.is_pressed('h'):
                vida = 100

            sleep(0.05)    
            system("cls")

    except KeyboardInterrupt:
        pass  # Captura a interrupção do teclado (CTRL+C) para sair do loop

    finally:
        keyboard.unhook_all()
        system("cls")

if __name__ == "__main__":
    main()
