def leiaint(num):
    while True:
        try:
            valor = int(input(num))
            break
        except:
            print('\033[0;31mERRO, DIGITE UM NÚMERO INTEIRO VALIDO\033[m')
    return valor


def leiafloat(num):
    while True:
        try:
            valor = float(input(num))
            break
        except:
            print('\033[0;31mERRO, DIGITE UM NÚMERO REAL VALIDO\033[m')
    return valor



i = leiaint('Digite um número inteiro: ')
r = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {i} e o número real foi {r}')