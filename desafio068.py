import random
from time import sleep

print('~'*15)
print('PAR OU ÍMPAR')
print('~'*15)

vitorias = 0

while True:
    soma = 0
    numeroc = random.randint(0,5)
    numeroj = int(input('Digite um valor entre 0 e 5: '))
    parimpar = input('Par ou ímpar [P/I] ').upper().strip()[0]
    print('~' * 30)
    if parimpar != 'P' and parimpar != 'I':
        print('Digite somente P ou I')
        print('~' * 30)
        
    soma = numeroj + numeroc
    if soma % 2 == 0 and parimpar == 'P':
        print(f'O computador escolheu {numeroc} e você {numeroj}. O total foi de {soma}, deu Par ')
        print('O úsuario venceu, continue o jogo')
        vitorias += 1
    elif soma % 2 == 0 and parimpar == 'I':
        print(f'O computador escolheu {numeroc} e você {numeroj}. O total foi de {soma}, deu Par')
        print('O úsuario perdeu, parando o jogo...')
        sleep(2)
        break
    elif soma % 2 == 1 and parimpar == 'P':
        print(f'O computador escolheu {numeroc} e você {numeroj}. O total foi de {soma}, deu Impar')
        print('O úsuario perdeu, parando o jogo...')
        sleep(2)
        break
    elif soma % 2 == 1 and parimpar == 'I':
        print(f'O computador escolheu {numeroc} e você {numeroj}. O total foi de {soma}, deu Impar')
        print('O úsuario venceu, continue o jogo')
        vitorias += 1
print(f'Você venceu {vitorias} vezes consecutivas')




