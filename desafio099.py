from time import sleep

def maior(*num):
    cont = maior = 0
    print('='*45)
    print('Analisando os números digitados...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram analisados {cont} no total')
    print(f'O maior valor informado foi o número {maior}')


maior(1, 10, 11, 2)
maior(1, 20)










