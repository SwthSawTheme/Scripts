# Crie uma função que receba um dicionario e calcula a media dos estudantes
# O dicionario tem como chave o nome do aluno e os valores são uma lista com as notas desses alunos

alunos = {
    "joão": [6,6,6],
    "maria": [4,6,3],
    "jose": [10,4,5]
}
def calc_media(alunos:dict):
    for item in alunos:
        media = sum(alunos[item]) / len(alunos[item])
        if media >= 6:
            print(f"{item}: Aprovado! Nota {media:.2f}")
        else:
            print(f"{item}: Reprovado! Nota {media:.2f}")


notas = calc_media(alunos)
