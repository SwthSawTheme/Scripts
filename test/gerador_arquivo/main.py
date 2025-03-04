def logs(error: str):
    try:
        with open("logs.txt", "a") as file:
            file.write(error + "\n")  # Adiciona nova linha e evita sobrescrever
        return "Log gerado com sucesso!"
    except OSError:
        return "Não foi possível gerar ou atualizar o arquivo de log!"

def file_generator(text: str):
    try:
        with open("settings.txt", "a") as file:
            file.write(f"{text}\n")
        return "Arquivo settings.txt atualizado com sucesso!"
    except OSError as e:
        log_message = f"Erro ao escrever no arquivo: {str(e)}\n"
        logs(log_message)
        return "Erro ao acessar o arquivo! Log gerado."

if __name__ == "__main__":
    text = str(input("Insira um dado: "))
    result = file_generator(text)
    print(result)