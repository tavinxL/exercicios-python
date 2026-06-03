import random
from time import sleep
from operator import itemgetter
ranking = dict()
p = 0
jogadores = {'jogador1': random.randint(1, 6),
             'jogador2': random.randint(1, 6),
             'jogador3': random.randint(1, 6),
             'jogador4': random.randint(1, 6),
                                                    }
for k, v in jogadores.items():
    print(f'O {k} tirou o número {v}')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print()
print('===RANKING DOS JOGADORES===')
print()
for j, l in enumerate(jogadores):
    p += 1
    print(f'{p}° Lugar - {ranking[j][0]} com {ranking[j][1]}')