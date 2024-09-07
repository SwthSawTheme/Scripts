

alunos = [
    {"nome": "Ana", "matematica": 7.5, "portugues": 8.0, "historia": 6.5},
    {"nome": "Carlos", "matematica": 5.5, "portugues": 6.0, "historia": 7.0},
    {"nome": "Beatriz", "matematica": 8.5, "portugues": 6.5, "historia": 7.0},
    {"nome": "João", "matematica": 6.0, "portugues": 6.5, "historia": 7.5}
]

def analisar_notas(alunos):
    notas = {
        "media": {},
        "acima_da_media": []
    }

    for i in alunos:
        media = (i["matematica"] + i["portugues"] + i["historia"]) / 3
        notas["media"][i["nome"]] = media
        if media >= 7:
            notas["acima_da_media"].append(i["nome"])

    return notas


if __name__ == "__main__":
    app = analisar_notas(alunos)
    print(app)