lista = ('Pão', 1,
         'Leite', 3.90,
         'Lapis', 1.20,
         'Mochila', 120.30,
         'Teclado', 130.99,
         'Mouse', 170,
         'Headset', 190.99)

print('=-'*17)
print('{:^30}' .format('LISTAGEM DE PREÇOS'))
print('=-'*17)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:.>4.2f}')
