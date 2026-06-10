def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols}(s) no campeonato')

n = str(input('Qual é o nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)