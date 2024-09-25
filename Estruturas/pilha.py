import os

class Pilha:
    def __init__(self):
        self.pilha = []
    
    def push(self,n):
        return self.pilha.append(n)
    
    def pop(self):
        return self.pilha.pop()
    
    def getPilha(self):
        return self.pilha
    
pilha = Pilha()

while True:
    print(pilha.getPilha())
    opcoes = ["1.push","2.pop","3.exit"]

    for i in opcoes:
        print(i)

    n = int(input())

    if n == 1:
        num = int(input("valor: "))
        pilha.push(num)
        os.system("cls")
    elif n == 2:
        pilha.pop()
        os.system("cls")
    elif n == 3:
        break