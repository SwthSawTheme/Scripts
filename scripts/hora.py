# Faça uma função que receba uma strind em hh:mm:ss (hora, minuto e segundo)
# E retorne o total em segundo

def hora(tempo:str):
    hora = int(tempo[0:2]) * 3600
    minuto = int(tempo[3:5]) * 60
    segundo = int(tempo[6:8])

    conv = hora + minuto + segundo
    return conv

tempo = hora("55:55:00")
print(tempo)