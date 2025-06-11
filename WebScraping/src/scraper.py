import requests
from bs4 import BeautifulSoup

# Fazendo a requisição para a página de notícias
url = r'https://www.rucoyonline.com/characters/Cant%20Lie'
response = requests.get(url)
html = response.text

# Criando o objeto Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Buscando todos os elementos que contêm os títulos das notícias
titulos = soup.find_all(class_="table-responsive")


characters = {}

for titulo in titulos:
    
    print(titulo.text.strip())