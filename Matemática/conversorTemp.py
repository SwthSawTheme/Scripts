
# Conversor de Fahrenheit para Celsius
def conversor(tf:float):
    return 5/9*(tf - 32)

if __name__ == "__main__":
    try:
        tf = float(input("Digite Grau Fahrenheit: "))
        result = conversor(tf)
        print(f"Grau Celsius: {result:.2f}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Processo finalizado...")