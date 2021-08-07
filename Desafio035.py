lado1 = float(input('Digite o tamanho do primeiro lado do triângulo: '))
lado2 = float(input('Digite o tamanho do segundo lado do triângulo: '))
lado3 = float(input('Digite o tamanho do terceiro lado do triângulo: '))
if lado1 < (lado2+lado3) and lado1 > (lado2-lado3):
    print('Essas medidas formam um triangulo')
else:
    print('Essas medidas não formam um triângulo')