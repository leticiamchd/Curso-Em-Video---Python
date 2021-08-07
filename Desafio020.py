import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1,aluno2,aluno3,aluno4] #Para criar uma lista, as opções precisam estar em colchetes
random.shuffle(lista) #Essa função ordena a lista de maneira aleatória
print('A ordem de apresentação será {}'.format(lista)) #Aqui estu escrevendo a lista já ordenada
