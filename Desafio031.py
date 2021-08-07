km = float(input('Qual a distância da viagem em km ? '))
if km > 200:
    print('O valor da viagem foi R${}'.format(0.45*km))
else:
    print('O valor da viagem foi R${}'.format(0.5*km))