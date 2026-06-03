from random import randint

num = (randint(1, 10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os números sorteados foram: ', end='')

for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior valor é o {max(num)} ')
print(f'O menor valor é o {min(num)} ')





