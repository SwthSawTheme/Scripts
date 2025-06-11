import requests
from bs4 import BeautifulSoup


character = str(input("Digite o nome do personagem: "))
character = character.strip("%20")
# Requisição da pagina
response = requests.get(f"https://www.rucoyonline.com/characters/{character}")
html = response.text


soup = BeautifulSoup(html,"html.parser")

table = soup.find("table", class_="character-table")

character_info = {}

for row in table.tbody.find_all('tr'):
    cols = row.find_all('td')
    key = cols[0].get_text(strip=True)
    value = cols[1].get_text(strip=True)
    character_info[key] = value


