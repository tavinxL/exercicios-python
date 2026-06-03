from math import factorial
from time import sleep

num = int(input('Digite um número que você deseja saber o fatorial: '))
print('CALCULANDO FATORIAL...')
sleep(1)
fatorial = factorial(num)
c = num
while c > 0:
    print(f'{num}', end='')
    if num > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    c -= 1
    num -= 1
print(fatorial)


