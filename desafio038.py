a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

if a > b:
    print('ANALISANDO OS NÚMEROS...')
    print('O PRIMEIRO valor é maior' .format(a, b))

elif a < b:
    print('ANALISANDO OS NÚMEROS...')
    print('O SEGUNDO valor é maior' .format(b, a))

else:
    print('ANALISANDO OS NÚMEROS...')
    print('Os dois VALORES são iguais' .format(a, b))
