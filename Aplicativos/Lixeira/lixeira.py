import winshell as wh
import time
try:
    wh.recycle_bin().empty(confirm=False, show_progress=True, sound=True)

    print("Lixeira foi esvaziada!")
    time.sleep(1)
    input("\n\nDesenvolvido by Swth...")
    
except:
    print("Lixeira vazia!!")
    time.sleep(1)
    input("\n\nDesenvolvido by Swth...")