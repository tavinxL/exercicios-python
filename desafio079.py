listanum = []

while True:
    n = int(input('Digite um número: '))
    if n not in listanum:
        listanum.append(n)
    else:
        print('Número duplicado, não podemos adicionar!')

    r = input('Você deseja adicionar mais algum número ? [S/N]').upper().strip()
    if r not in 'Ss':
        break
print(f'Voce digitou os numeros {sorted(listanum)}')


