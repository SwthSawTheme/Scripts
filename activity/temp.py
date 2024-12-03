import numpy as np

def coletar_dados():
    # Inicializa o array bidimensional
    cidades = []

    # Coleta os dados das 10 cidades
    for i in range(10):
        print(f"\nCidade {i + 1}:")
        temp_max = float(input("Digite a temperatura máxima (°C): "))
        temp_min = float(input("Digite a temperatura mínima (°C): "))
        umidade = float(input("Digite a umidade (%): "))
        cidades.append([temp_max, temp_min, umidade])

    # Converte para um array numpy para facilitar os cálculos
    cidades_array = np.array(cidades)
    return cidades_array

def processar_dados(cidades_array):
    # Exibe todos os valores armazenados
    print("\nDados das cidades (Temp. Máx., Temp. Mín., Umidade):")
    for i, cidade in enumerate(cidades_array, start=1):
        print(f"Cidade {i}: {cidade}")

    # Calcula a maior temperatura máxima
    maior_maxima = np.max(cidades_array[:, 0])
    # Calcula a menor temperatura mínima
    menor_minima = np.min(cidades_array[:, 1])
    # Calcula a média da umidade
    media_umidade = np.mean(cidades_array[:, 2])

    # Exibe os resultados
    print(f"\nMaior temperatura máxima: {maior_maxima:.2f}°C")
    print(f"Menor temperatura mínima: {menor_minima:.2f}°C")
    print(f"Média da umidade: {media_umidade:.2f}%")

# Coleta os dados
cidades_array = coletar_dados()
# Processa e exibe os resultados
processar_dados(cidades_array)
