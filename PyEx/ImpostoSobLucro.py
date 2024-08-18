# ### 1- Imposto a pagar no Lucro Presumido

# - 5% sobre faturamento de ISS (mensal)
# - 0,65% de PIS sobre faturamento, (mensal)
# - 3% de COFINS sobre faturmaneto, (mensal)
# - 4.8% de IR (trimestral)
# - 10% de IR Adicional sobre o que ultrapassar 20mil do faturamento (trimestral)
# - CSLL: 2,88% sobre faturamento (trimestral)

faturamento = {
    'jan': 'R$ 95.141,98',
    'fev': 'R$ 95.425,16',
    'mar': 'R$ 89.716,31',
    'abr': 'R$ 78.459,99',
    'mai': 'R$ 71.087,28',
    'jun': 'R$ 83.911,06',
    'jul': 'R$ 56.467,26',
    'ago': 'R$ 88.513,58',
    'set': 'R$ 66.552,49',
    'out': 'R$ 80.164,07',
    'nov': 'R$ 66.964,33',
    'dez': 'R$ 71.525,25',
}

# você precisa inserir no sistema um dicionário no formato:

#     'mes': (faturamento, imposto_mensal, imposto_trimestral),
# }
resultado = {}
# Passo a passo
# Percorrer o dicionario de faturamento
    # Transformar o faturamento dos meses em um número inteiro
    # calcular o imposto mensal
    # calcular o imposto trimestral
    # adicionar a um dicionario o faturamento, imposto mensal e o imposto trimestral em uma tupla

# Converte os valores de um dicionario de string para int!
def transformString(texto):
    texto = texto.replace("R$","")
    texto = texto.replace(".","")
    texto = texto.replace(",",".")
    valor = float(texto)
    return valor
# - 5% sobre faturamento de ISS (mensal)
# - 0,65% de PIS sobre faturamento, (mensal)
# - 3% de COFINS sobre faturmaneto, (mensal)

def impostoMensal(valor):
    iss = valor * 0.05
    pis = valor * 0.0065
    cofins = valor * 0.03
    total = iss + pis + cofins
    return total

# - 4.8% de IR (trimestral)
# - 10% de IR Adicional sobre o que ultrapassar 20mil do faturamento (trimestral)
# - CSLL: 2,88% sobre faturamento (trimestral)

def impostoTrimestral(valor):
    ir = valor * 0.048
    csll = valor * 0.0288    
    ir_adicional = 0
    if ir_adicional >= 20000:
        ir_adicional = (valor - 20000) * 0.1
    imposto = ir + csll + ir_adicional
    return imposto

def main():
    for mes, valor in faturamento.items():
        valor = transformString(valor)
        valor_impostoMensal = impostoMensal(valor)
        valor_impostoTrimestral = impostoTrimestral(valor)
        resultado[mes] = (valor,valor_impostoMensal,valor_impostoTrimestral)
    print(resultado)
        

if __name__ == "__main__":
    main()