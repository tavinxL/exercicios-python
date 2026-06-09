from random import randint
from time import sleep

lista = list()
def sorteia():
    print('Sorteando 5 valores aleatórios...', flush=True)
    sleep(0.6)
    print('=-'*30)
    for c in range(1, 6):
        lista.append(randint(1, 100))
    print(f'Os valores sorteados foram: ',end='', flush=True)
    for valor in lista:
        print(f'{valor}', end=' ', flush=True)
    print()
    sleep(0.6)

def somapar():
    print('=-' * 30)
    print('Somando os valores da lista, somente os pares...', flush=True)
    sleep(0.6)
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Os valores pares, somados na lista é igual a {soma}', flush=True)

sorteia()
somapar()