# Define uma classe chamada DVD
class DVD:
    # O método __init__ é o construtor da classe, que inicializa os atributos do DVD
    def __init__(self, name, release_year, director):
        self.name = name           # Nome do DVD
        self.release_year = release_year  # Ano de lançamento do DVD
        self.director = director   # Diretor do DVD

    # Define como o objeto DVD deve ser representado quando convertido em string
    def __str__(self):
        return f"{self.name}, dirigido por {self.director}, lançado em {self.release_year}"

# Cria uma lista vazia para armazenar DVDs
lista_de_DVD = []

# Cria um objeto DVD com nome "Jogos mortais", ano de lançamento "2010" e diretor "James Wan"
dvd = DVD("Jogos mortais", "2010", "James Wan")

# Adiciona o objeto DVD à lista de DVDs
lista_de_DVD.append(dvd)

# Define uma lista chamada quadrados com 10 índices, inicializados com 0
quadrados = [0] * 10

# Preenche a lista quadrados com os quadrados dos números de 1 a 10
for i in range(10):
    quadrado = (i + 1) ** 2   # Calcula o quadrado de (i+1)
    quadrados[i] = quadrado   # Atribui o valor do quadrado ao índice i da lista quadrados

# Imprime a lista quadrados para mostrar os valores calculados
print(quadrados)
