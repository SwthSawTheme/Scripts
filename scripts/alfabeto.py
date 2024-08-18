# Faça uma funlçao, que receba um valor entre 1 e 26 e retorne as letras do alfabeto
import string

def alfabeto(num:int):
    """
    Retorna um valor representado nas letras do alfabeto.

    Args:
    num (int): um número inteiro entre 1 e 26.

    Returns:
    list(str): uma lista de letras do alfabeto até o número fornecido.

    Raises:
    ValueError: se o número não estiver dentro do intervalo de 1 e 26.
    """
    if num >= 1 and num <= 26:
        return list(string.ascii_uppercase[:num])
    else:
        raise ValueError("Digite um inteiro entre 1 e 26")


try:
    num = int(input())
    alfabeto(num)
except ValueError as e:
    print(e)