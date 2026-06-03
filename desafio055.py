print('===MAIOR E MENOR===')
print()

for c in range(1, 6):
    p = float(input(f'Qual é o peso da {c}ª pessoa?: '))

    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p

        if p < menor:
            menor = p

print()
print(f'O maior peso digitado foi {maior} kg.')
print(f'O menor peso digitado foi {menor} kg.')
