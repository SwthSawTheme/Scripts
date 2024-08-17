# O que é um número primo?
# Um número primo é um número maior que 1 que só pode ser dividido por 1 e por ele mesmo.
# Em outras palavras, ele tem exatamente dois divisores: 1 e o próprio número.

# Passos para criar a função:
# Receber o número: A função precisa receber um número como entrada.
# Verificar se o número é menor que 2: Qualquer número menor que 2 (ou seja, 1 e 0) não é primo.
# Verificar divisores: Para números maiores que 2, verificamos se existe algum divisor que seja diferente de 1 e do próprio número.
# Isso pode ser feito dividindo o número por todos os inteiros de 2 até a raiz quadrada do número.
# Retornar o resultado: Se encontrarmos um divisor, o número não é primo. Se não encontrarmos nenhum divisor, o número é primo.
import math

# Função que retorna se o número é primo ou não!
def isPrimo(num):
    # Verifica se o número é menor que 2
    if num < 2:
        return False

    # Calcula se o número é divisível baseado na sua raiz quadrada!
    for n in range(2, int(math.sqrt(num) + 1)):
        # Se o resto da divisão for igual a 0, significa que ele não é primo
        if num % n == 0:
            return False
    # Retorna se o número é primo caso as afirmativas a cima retornarem verdadeiro
    return True

# Inicia um loop
while True:
    # Atribui um metodo de entrada para a variavel num
    num = int(input())
    # Passa a variável num para a função IsPrimo()
    primo = isPrimo(num)
    # Imprime na tela o retorno da váriavel primo
    print(primo)
