km = float(input('Qual a velocidade do carro ? '))
if km > 80:
    print('Você foi multado. O valor da multa é de R${}'.format((km-80)*7))
else:
    print('Você estava dentro do limite de velocidade, continue assim!')