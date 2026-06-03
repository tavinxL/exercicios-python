
pessoas = list()
dados = list()
totpessoas = 0
maior = menor = 0


while True:
    pessoas.append(input('Nome: '))
    totpessoas += 1
    pessoas.append(int(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()

    r = input('Você deseja adicionar mais alguem ? [S/N]: ').upper().strip()
    if r not in 'Ss':
        break


print(f'Foram cadastradas {totpessoas} pessoas')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in dados:
    if p[1] == maior:
        print(f'{p[0]}, ', end='')
print()
print(f'O menor peso é de {menor}kg. Peso de ', end='')
for p in dados:
    if p[1] == menor:
        print(f'{p[0]}, ', end='')



