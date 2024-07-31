# Faça uma funlçao, que receba um valor entre 1 e 26 e retorne as letras do alfabeto
import string

def alfabeto(num:int):
    if num > 1 and num < 26:
        alfa = [string.ascii_uppercase]

num = int(input)
alfa = [string.ascii_uppercase[:num]]