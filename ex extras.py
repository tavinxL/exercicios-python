from random import randint

escolhacomputador = randint(1, 20)
print('Escolha um número de 1 a 20, e tente advinhar qual número o computador escolheu, '
      'você tem 5 tentativas: ')


for c in range(1, 6):
    escolhausuario = int(input(' '))
    if escolhacomputador > escolhausuario:
        print('O número é maior...')
    elif escolhacomputador < escolhausuario:
        print('O número é menor...')
    else:
        print('Parabens, você acertou')
        break
else:
    print(f'Você perdeu, o número era {escolhacomputador}')
