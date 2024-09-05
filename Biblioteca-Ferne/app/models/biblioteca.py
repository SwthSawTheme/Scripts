
class Biblioteca(object):

    def __init__(self,livro:list):
        self.livros = []

    def adicionar_livro(self,livro):
        return self.livros.append(livro)
    
    def listar_livros(self):
        for i in self.livros:
            print(i)

    def salvar_em_arquivo(self):
        try:
            with open("biblioteca.txt", "w") as livro:
                for i in self.livros:
                    livro.write(f"{i}\n")
        except FileExistsError:
            return print("Arquivo já existe!")
    
    def carregar_arquivo(self,arquivo):
        try:
            with open(f"{arquivo}.txt","r") as livro:
                livro = livro.read()
                return self.livros.append(livro)
        except FileNotFoundError:
            return print("Arquivo não encontrado!")


    