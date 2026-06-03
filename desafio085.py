lista = [[], []]

for c in range(1, 8):
    num = int(input(f'Digite o {c}o. valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
sorted(lista[0])
sorted(lista[1])

print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')

