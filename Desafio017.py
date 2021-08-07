from math import sqrt,pow
num1 = float(input('Digite o tamanho de um cateto: '))
num2 = float(input('Digite o tamanho do outro cateto: '))
hip = sqrt(pow(num1,2)+pow(num2,2))
print('O valor da hipotenusa é de {}'.format(hip))