from datetime import date

print('===MAIORIDADE===')
print()
ma = 0
me = 0
atual = date.today().year

for c in range(1, 8):
    p = int(input(f'Em que ano a {c} pessoa nasceu ?: '))
    idade = atual - p
    if idade >= 18:
        ma = ma + 1
    else:
        idade = atual - p
        me = me + 1
print(f'São {ma} pessoas que possuem a maioridade\nE {me} pessoas que não possuem a maioridade')




