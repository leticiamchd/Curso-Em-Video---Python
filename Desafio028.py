import random
num = random.randint(0,5)
num2 = int(input('Digite um numero de 0 a 5: '))
if num == num2 :
    print('Parabéns, você advinhou o número')
else:
    print('Não foi dessa vez que você advinhou o número, tente outra vez')