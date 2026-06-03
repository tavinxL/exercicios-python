

listanum = []
listapar = []
listaimpar = []
while True:
    num = int(input('Digite um número: '))
    listanum.append(num)

    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)

    r = input('Voce deseja adicionar mais algum número ? [S/N]: ').upper().strip()
    if r not in 'Ss':
        break

print(f'A lista principal é {sorted(listanum)}')
print(f'A lista de números pares é {sorted(listapar)}')
print(f'A lista de números ímpares é {sorted(listaimpar)}')