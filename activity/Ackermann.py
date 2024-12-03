def ackermann(m, n):
    """Calcula a função de Ackermann para inteiros não negativos m e n."""
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

# Programa principal
if __name__ == "__main__":
    print("Função de Ackermann")
    
    try:
        # Coleta os valores de m e n do usuário
        m = int(input("Digite o valor de m (inteiro não negativo): "))
        n = int(input("Digite o valor de n (inteiro não negativo): "))
        
        # Valida se os valores são não negativos
        if m < 0 or n < 0:
            print("Por favor, insira apenas valores inteiros não negativos.")
        else:
            # Calcula e exibe o resultado
            resultado = ackermann(m, n)
            print(f"O resultado de A({m}, {n}) é: {resultado}")
    except RecursionError:
        print("Erro: a função atingiu o limite de recursão. Os valores de m e n podem ser muito grandes.")
    except ValueError:
        print("Por favor, insira apenas valores inteiros não negativos.")
