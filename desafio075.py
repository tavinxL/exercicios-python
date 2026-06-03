valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite outro número: ')))
print('=-'*30)
print(f'Você digitou os seguintes valores: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 not in valores:
    print('O valor 3 não apareceu em nenhuma posição')
else:
    print(f'O valor 3 apareceu na posição {valores.index(3)}ª')

print(f'Os valores pares digitados foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(f'{n}', end=' ')





