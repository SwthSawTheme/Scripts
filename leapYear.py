# Crie uma função que retorne se um ano é bissexto ou não!

def leepYer(year:int):
    if year % 4 == 0:
        print("É")
    else:
        print("Não é")

leepYer(2000)