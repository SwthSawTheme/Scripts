
def media(list):
    media = sum(list) / len(list)
    maior = max(list)
    menor = min(list)
    print(f"Media geral:{media}\nMaior nota:{maior}\nMenor nota:{menor}")

if __name__ == "__main__":
    lista = [3,4,5,6]
    media(lista)