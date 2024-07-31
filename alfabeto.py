# Faça uma funlçao, que receba um valor entre 1 e 26 e retorne as letras do alfabeto
import string

def alfabeto(num:int):
    if num > 1 and num < 26:
        alfa = list(string.ascii_uppercase[:num])
        return print(alfa)
    else:
        return Exception("Digite um inteiro entre 1 e 26")

num = int(input())
alfabeto(num)