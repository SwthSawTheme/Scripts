
class Biblioteca(object):

    def __init__(self,livro:list):
        self.livros = []

    def adicionar_livro(self,livro):
        return self.livros.append(livro)
    
    def listar_livros(self):
        for i in self.livros:
            print(i)

    def salvar_em_arquivo(self):
        with open("biblioteca.txt", "w") as livro:
            for i in self.livros:
                livro.write(f"{i}\n")
    
    def carregar_arquivo(self):
        with open("biblioteca.txt","r") as livro:
            livro = livro.read()
            return self.livros.append(livro)

livros = []
usf = Biblioteca(livros)

if __name__ == "__main__":
    usf.adicionar_livro("It - A Coisa")
    usf.adicionar_livro("O gato preto")
    usf.listar_livros()
    usf.salvar_em_arquivo()