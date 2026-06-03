times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Sao Paulo', 'Atletico PR', 'Bragantino', 'Coritiba', 'Bahia', 'Botafogo', 'Atletico MG',
         'Inter', 'Vasco', 'Cruzeiro', 'Vitoria', 'Gremio', 'Santos', 'Corinthians', 'Remo', 'Mirassol', 'Chapecoense')

print(f'Tabela do brasileirão 2026: {times}')
print('=-'*30)

print(f'Os 5 primeiros colocados do campeonato são: {times[:5]}')
print('=-'*30)

print(f'Os 4 ultimos são: {times[-4:]}')
print('=-'*30)

print(f'Os times em ordem alfabeticas: {sorted(times)}')
print('=-'*30)

print(f'O time da chapecoense esta na {times.index('Chapecoense')+1}ª posição')



