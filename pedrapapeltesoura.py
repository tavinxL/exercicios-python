import random

escolhas = ['r','p','s']
jogada = {'r':'Pedra', 'p':'Papel', 's':'Tesoura'}
escolhapc = random.choice(escolhas)
escolhauser = str(input('Você quer Pedra, Papel ou Tesoura (r/p/s) ?:')).strip()
if escolhauser not in escolhas:
    print('ERRO, JOGADA INVALIDA')

print('Você escolheu: {}{}{}' .format('\033[31m' ,jogada[escolhauser], '\033[m'))
print('O computador escolheu: {}{}{}' .format('\033[34m',jogada[escolhapc], '\033[m'))

if escolhauser == escolhapc:
    print('\033[36m Empate \033[m')

elif escolhauser == 'r' and escolhapc == 's':
    print('\033[35m O usuario venceu \033[m')

elif escolhauser == 'p' and escolhapc == 'r':
    print('\033[35m O usuario venceu \033[m')

elif escolhauser == 's' and escolhapc == 'p':
    print('\033[35m O usuario venceu \033[m')

else:
    print('\033[33m O computador ganhou \033[m')

print('---FIM---')
