import csv

def ler_arquivo_csv(nome_arquivo):
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            cabecalho = next(leitor)  # Lê o cabeçalho
            print(f"{'Descrição':<20}{'Unidade':<10}{'Quantidade':<15}{'Valor Unitário':<15}{'Valor Total':<15}")
            print("-" * 75)

            soma_valor_total = 0

            for linha in leitor:
                descricao, unidade, quantidade, valor_unitario, valor_total = linha
                soma_valor_total += float(valor_total)
                print(f"{descricao:<20}{unidade:<10}{quantidade:<15}{valor_unitario:<15}{valor_total:<15}")

            print("\n" + "-" * 75)
            print(f"Valor total de todos os itens: R$ {soma_valor_total:.2f}")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

# Nome do arquivo CSV
nome_arquivo = "produtos_supermercado.csv"

# Executa o programa
ler_arquivo_csv(nome_arquivo)

