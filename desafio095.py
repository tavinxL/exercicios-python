jogadores = []

continuar = 'S'

while continuar.upper() == 'S':
    gols = []

    nome = input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {nome} jogou? '))

    for g in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {g}? ')))

    jogadores.append({
        'nome': nome,
        'gols': gols,
        'total': sum(gols)
    })

    continuar = input('Quer continuar? [S/N] ')
    print('-' * 40)

# Tabela de jogadores
print('=' * 55)
print(f'{"cod":<5} {"nome":<20} {"gols":<20} {"total"}')
print('-' * 55)

for cod, jogador in enumerate(jogadores):
    print(f'  {cod:<4} {jogador["nome"]:<20} {str(jogador["gols"]):<20} {jogador["total"]}')

print('-' * 55)

# Levantamento individual
while True:
    try:
        cod = int(input('\nMostrar dados de qual jogador? '))
        jogador = jogadores[cod]
        print(f'\n-- LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
        for i, g in enumerate(jogador['gols']):
            print(f'      No jogo {i} fez {g} gols.')
    except (IndexError, ValueError):
        print('Código inválido. Tente novamente.')