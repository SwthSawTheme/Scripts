

class Livro(object):

    def __init__(self,titulo:str,autor:str,ano_publicacao:str):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def getBook(self):
        formato = [f"Titulo: {self.titulo}",
                   f"Autor: {self.autor}",
                   f"Publicação:{self.ano_publicacao}"
                   ]
        
        for l in formato:
            print(l)


itAcoisa = Livro("It - A Coisa","Stephan King"," fev de 1999")


if __name__ == "__main__":
    itAcoisa.getBook()