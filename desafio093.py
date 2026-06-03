jogadordefut = dict()
gol = list()
nomej = input('Qual o nome do jogador ?: ')
jogadordefut['Nome'] = nomej
partidasj = int(input(f'Quantas partidas {nomej} jogou ?:'))
print('=-'*20)


for g in range(0, partidasj):
    gol.append(int(input(f'Quantos gols na partida{g} ?:')))

jogadordefut['Golsm'] = gol
jogadordefut['Total'] = sum(gol)
print('=-'*20)

for k, v in jogadordefut.items():
    print(f'O campo {k} tem valor {v}')
print('=-'*20)

print(f'O jogador {nomej} jogou {partidasj} partidas.')
for p, g in enumerate(gol):
    print(f' => Na partida{p}, ele marcou {g} gols')
print(f'Foi um total de {jogadordefut['Total']} gols')


