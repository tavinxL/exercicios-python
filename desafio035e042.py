print('---ANALISANDO TRIANGULO---')
r1 = float(input('Digite o comprimento dessa reta 1: '))
r2 = float(input('Digite o comprimento dessa reta 2: '))
r3 = float(input('Digite o comprimento dessa reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas conseguem formar um triângulo')
    print()

    if r1 == r2 == r3:
        print('Formará um triãngulo equilátero, todos os lados iguais')

    elif r1 != r2 != r3 != r1:
        print('Formará um triângulo escaleno, todos os lados diferentes')
    else:
        print('Formará um triãngulo isóceles, dois lados iguais')

else:
    print('Essas retas não conseguem formar um triângulo')
print('---FIM---')
