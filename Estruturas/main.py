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

print(menor,maior)