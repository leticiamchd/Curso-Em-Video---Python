nome = input('Digite o seu nome: ')
separado = nome.split()
print('Seu primeiro nome é {}'.format(separado[0]))
print('Seu último nome é {}'.format(separado[len(separado)-1]))
