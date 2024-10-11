import pyautogui
import time

# Função para alternar para a próxima janela com Alt + Tab
def alt_tab():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')

# Função para rolar para baixo e para cima
def scroll_page(scrolls, direction='down'):
    if direction == 'down':
        pyautogui.scroll(-scrolls)
    elif direction == 'up':
        pyautogui.scroll(scrolls)

# Função principal que executa as ações infinitamente
def automate_action():
    # Executa Alt + Tab apenas uma vez para alternar para a janela desejada
    alt_tab()  
    time.sleep(1)  # Espera um segundo para garantir que a janela mudou
    
    while True:  # Loop infinito
        # Clica no centro da tela
        width, height = pyautogui.size()
        pyautogui.click(width // 2, height // 2)
        
        # Rola para baixo
        scroll_page(scrolls=5000, direction='down')
        
        # Espera 5 minutos
        time.sleep(300)

        # Rola para cima
        scroll_page(scrolls=5000, direction='up')

# Executa a automação infinitamente
automate_action()
