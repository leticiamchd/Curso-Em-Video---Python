ano = int(input('Digite o ano: '))
ano2 = ano %4
if ano2 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))