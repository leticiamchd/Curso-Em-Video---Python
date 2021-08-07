dias = int(input('Quantos dias de aluguel do carro ? '))
km = float(input('Quantos km percorridos no total ? '))
print('O valor total do aluguel foi de R${}'.format(dias*60+km*0.15))