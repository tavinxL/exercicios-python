# Sistema de Ranking de Jogadores
# Cadastra jogadores, ordena por pontuação,
# mostra pódio, e calcula média

jogadores = []
maior = menor = 0
# Cadastro de 5 jogadores
for c in range(1, 6):
    nome = input(f'Digite o nome do jogador {c}: ')
    pontos = int(input(f'Digite a pontuação de {nome}: '))
    jogadores.append([nome, pontos])

# Ordenar do maior para menor
jogadores_ordenados = sorted(jogadores, key=lambda x: x[1], reverse=True)

# Listar ranking
print('\n=== RANKING ===')
for i in range(len(jogadores)):
    print(f'{i+1}º lugar: {jogadores_ordenados[i][0]} - {jogadores_ordenados[i][1]} pontos')

# Mostrar pódio (top 3)
print('\n=== PÓDIO ===')
podio = jogadores_ordenados[:3]
for i, p in enumerate(podio):
    print(f'{i+1}º lugar - {p[0]}')

# Média de pontuação
total = 0
for j in jogadores:
    total += j[1]
media = total / len(jogadores)
print(f'\nMédia de pontuação: {media:.2f}')