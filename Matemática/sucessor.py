
def sucessor(n:int):
    return n + (n + 1)

if __name__ == "__main__":
    print("A soma de dois números consecutivos")
    n = int(input())
    print(sucessor(n))