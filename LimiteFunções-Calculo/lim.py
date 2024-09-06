def limite(x):
    x = ((x**2) - (5*x) + 6) / ((x**2)-4)
    return x

while True:
    print("Limites da f(x)")
    x = float(input())
    y = limite(x)
    print(y)