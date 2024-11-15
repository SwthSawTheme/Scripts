# Problema
# A empresa TMJ tem uma plataforma que gera enquetes para seus usuários.

# Sua tarefa é desenvolver um algoritmo que recebe a lista de respostas
# e retorne a resposta mais votada e a quantidade de votos.

# O seu metodo precisa retornar uma lista onde a primeira posição é a resposta
# mais selecionada e a segunda posição a quantidade.


# Saida esperada:
"""
respostas = [
    "manha",
    "manha",
    "tarde",
    "noite",
    "tarde",
    "noite",
    "manha",
]

Resultado: ['manha', 3]
"""

# desenvolva sua solução aqui
from collections import Counter

def solucao(respostas):
    contagem = Counter(respostas)
    mais_votada, votos = contagem.most_common(1)[0]  # Pega a resposta mais votada e seu número de votos
    return [mais_votada, votos]


# Executando testes da sua função
teste_enquete_1 = [ "dia", "tarde", "dia", "noite", "noite", "tarde", "dia", "noite", "dia", "tarde" ]
teste_enquete_2 = [ "cachorro", "papagaio", "gato", "gato", "cavalo", "cachorro", "abelha", "formiga", "formiga", "cavalo", "gato", "papagaio", ]
teste_enquete_3 = [ "carro", "bicicleta", "bicicleta", "moto", "moto", "moto", "moto", "carro", "bicicleta", "onibus", "onibus", "carro", ]

print(f"[teste_enquete_1] {'passou' if solucao(teste_enquete_1) == ['dia', 4] else 'falhou'}")
print(f"[teste_enquete_2] {'passou' if solucao(teste_enquete_2) == ['gato', 3] else 'falhou'}")
print(f"[teste_enquete_3] {'passou' if solucao(teste_enquete_3) == ['moto', 4] else 'falhou'}")