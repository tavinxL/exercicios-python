print('~'*30)
print('        TABUADA v3.0')
print('~'*30)

while True:
    print()
    num = int(input('Digite o número que você deseja saber a tabuada [Digite um número negativo para sair do programa]: '))
    print()
    print('=' * 30)

    if num < 0:
        break
    print('=' * 30)

    for c in range(1, 11):
        resultado = num * c
        print(f'{num} x {c} = {resultado}')
    print('=' * 30)











