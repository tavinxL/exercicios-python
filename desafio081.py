
print('=-'*7)
print('   LISTA   ')
print('=-'*7)

listanum = []
while True:
    num = int(input('Digite um número: '))
    listanum.append(num)

    r = input('Voce deseja adicionar mais algum número ? [S/N]: ').upper().strip()
    if r not in 'Ss':
        break

print(f'Foram digitados {len(listanum)} números')
print('=-'*20)

listanum.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é {listanum}')
print('=-'*20)

if 5 in listanum:
    print('O valor 5 foi digitado e esta na lista')
else:
    print('O valor 5 nao foi digitado e não esta na lista')

