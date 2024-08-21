# Estruturas de Dados para iniciantes

# Exercício 1: Crie uma lista que contenha os números de 1 a 10 e imprima todos os números.

lista = [1,2,3,4,5,6,7,8,9,10]
#print(lista)

# Exercício 2: Adicione os números 11 e 12 ao final da lista e imprima a lista atualizada.
lista.append(11)
lista.append(12)
#print(lista)

# Exercício 3: Remova o número 5 da lista e imprima a lista.
lista.remove(5)
#print(lista)

# Exercício 4: Inverta a ordem da lista e imprima o resultado.

lista.reverse()
# print(lista)

# Exercício 5: Encontre o maior e o menor número na lista.

menor = min(lista)
maior = max(lista)

#print(menor,maior)

## Pilhas (Stacks)

#Exercício 1: Implemente uma pilha usando uma lista. Inclua operações para empilhar (push) e desempilhar (pop) elementos.

import os
import time

class Pilha:

    def __init__(self):
        self.pilhas = []

    def push(self,objeto):
        self.pilhas.append(objeto)

    def pop(self):
        if self.pilhas:
            return self.pilhas.pop()
        else:
            return None


def main():

    pilha = Pilha()

    while True:

        print(f"Conteudo da pilha {pilha.pilhas}")

        item =  input("Digite um item para adicionar a pilha ou exit para sair: ")
        if item == "exit":
            break


        if item in pilha.pilhas:
            pilha.pop()
            print("Desempilhando!")
        else:
            pilha.push(item)
            print("Empilhando")

        os.system("cls")
        time.sleep(0.05)

if __name__ == "__main__":
    main()