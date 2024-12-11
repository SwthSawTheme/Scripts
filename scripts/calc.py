def calc(itens):
    total = 0
    for item in itens:
        subtotal = item * 2
        total += subtotal
    return total


valor = [3,5,2,7]
resultado = calc(valor)
print(resultado)