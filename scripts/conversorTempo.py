# Crie uma função que receba 
# o tempo no formato 
# tempo(str) = "hh:mm:ss "
# e retorne o valor em segundos


def conversorTempo(num:str):
    horas, minutos, segundos = map(int,num.split(":"))
    return horas * 3600 + minutos * 60 + segundos


if __name__ == "__main__":
    print(conversorTempo("01:44:22"))