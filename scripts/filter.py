# Crie uma função que filtre uma lista de dicionarios de produtos
# Os inputs serão o dicionario, valor minimo e o valor maximo
# A função deve retornar um dicionario dentro desse intervaldo de preço

produtos = {
    "celular": 2000,
    "Tv LCD": 4999,
    "Banana": 30,
    "Sova": 49,
    "Coquitel": 87,
    "carne": 200,
    "coca cola": 13,
    "bolacha": 4,
    "pastel": 15,
    "trigo": 12
}

def filter(produtos:dict, minimo:int, maximo:int):
    novo_filtro = {}
    for item in produtos:
        if produtos[item] >= minimo and produtos[item] <= maximo:
            novo_filtro[item] = produtos[item]
    return novo_filtro

filtrar = filter(produtos, 56, 5000)

print(filtrar)