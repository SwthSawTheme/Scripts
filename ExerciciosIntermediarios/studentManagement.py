import os

def adicionar_aluno(aluno:str,notas:list[float],notas_alunos:dict[str,list[float]]):
    notas_alunos[f"{aluno}"] = notas

def calcular_media(notas:list[float]) -> float:
    media = sum(notas) / len(notas)
    return media

def maior_media(notas_alunos:dict[str,list[float]]) -> str:
    maior_Media = []
    nome_aluno = []
    for aluno, notas in notas_alunos.items():
        media = calcular_media(notas)
        maior_Media.append(media)
        nome_aluno.append(aluno)
    indice = maior_Media.index(max(maior_Media))
    return nome_aluno[indice]

def listar_alunos_medias(notas_alunos:dict[str,list[float]]):
    for aluno, nota in notas_alunos.items():
        media = calcular_media(nota)
        print(f"{aluno}:{media}")

def clear():
    try:
        os.system("cls")
    except:
        os.system("clear")

def save(dado,nome,notas):
    try:
        dado[f"{nome}"] = notas
        with open("settings.txt","w") as arquivo:
            arquivo.write(f"{dado}")
            print("Salvo com sucesso!")
    except:
        return print("Ocorreu um erro ao salvar!")

def load(dado):
    try:
        with open("settings.txt","r") as arquivo:
            arquivo = arquivo.read()
            return dado.update(eval(arquivo))
        
    except Exception as a:
        return print(f"Erro ao carregar! {a}")

def main():
    notas_alunos = {}

    while True:
        load(notas_alunos)
        opcoes = ["1. Adicionar um novo aluno com suas notas","2. Encontrar o aluno com a maior média", "3. Listar todos os alunos e suas médias","4. Sair"]

        for i in opcoes:
            print(i)
        choice = int(input())

        if choice == 1:
            clear()
            nome = input("Digite o nome do aluno: ")
            notas = []
            for i in range(3):
                nota = float(input(f"Digite a nota {i+1}: "))
                notas.append(nota)
            save(notas_alunos,nome,notas)
            notas_alunos[f"{nome}"] = notas
            print("Aluno registrado com sucesso!")
            input()
            clear()

        elif choice == 2:
            clear()
            print(maior_media(notas_alunos))
            input()
            clear()

        elif choice == 3:
            clear()
            listar_alunos_medias(notas_alunos)
            input()
            clear()

        elif choice == 4:
            break

if __name__ == "__main__":
    main()
    