salario = float(input('Digite o seu salário: '))
if salario <=1250 :
    print('O valor do seu aumento será de R${}'.format(salario*0.15))
else:
    print('O valor do seu aumento será de R${}'.format(salario*0.10))