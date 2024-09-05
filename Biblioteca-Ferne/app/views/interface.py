import os
import time
from app.models.biblioteca import Biblioteca
from app.models.livro import Livro

livros = []
biblioteca = Biblioteca(livros)

def adicionarLivro():
    titulo = input("Digite o titulo: ")
    autor = input("Digite o autor: ")
    ano = input("Digite o ano: ")
    livro = Livro(titulo,autor,ano)
    biblioteca.adicionar_livro(livro.titulo)

def listarLivros():
    return biblioteca.listar_livros()

def salvarLivros():
    return biblioteca.salvar_em_arquivo()

def carregarLivros():
    arquivo = input("Nome do Arquivo: ")
    return biblioteca.carregar_arquivo(arquivo)

def limpar_tela():
    # Limpa a tela do terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def app():

    while True:
        limpar_tela()
        opcoes = [
            "1. Adicionar livro (título,autor,ano)",
            "2. Listar todos os livros",
            "3. Salvar lista de livros em um arquivo",
            "4. Carregar uma lista de livros",
            "5. Sair"
            ]
        for i in opcoes:
            print(i)
        

        choice = int(input())

        if choice == 1:
            adicionarLivro()
        elif choice == 2:
            listarLivros()
            input()
        elif choice == 3:
            salvarLivros()
        elif choice == 4:
            carregarLivros()
        elif choice == 5:
            break

if __name__ == "__main__":
    app()