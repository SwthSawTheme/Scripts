# Faça uma função que receba uma string e transforme cada letra da string em um numero
# com a seu respectivo indice do alfabero
import string

def cryp(text:str):
    alfa = list(string.ascii_lowercase)
    texto = list(text)
    cript = ""
    for letra in texto:
        index = alfa.index(letra) + 1
        cript += str(index) 

    return cript
            

senha = cryp("sawtheme")
print(senha)