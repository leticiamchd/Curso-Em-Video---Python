num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
lista = [num1,num2,num3]
ordem = sorted(lista)
print(lista)
print(ordem)
print('O número {} é o maior'.format(ordem[2]))
print('O número {} é o menor'.format(ordem[0]))