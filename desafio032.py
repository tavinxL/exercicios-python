print('---ANO BISSEXTO---')
ano = int(input('Digite um ano: '))
print('O ano digitado foi {}' .format(ano))
if ano == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é ano bissexto' .format(ano))
else:
    print('{} não é ano bissexto' .format(ano))
print('---FIM---')