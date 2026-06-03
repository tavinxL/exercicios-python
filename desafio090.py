escola = dict()

escola['Nome'] = str(input('Nome: '))
escola['Media'] = float(input(f'Média de {escola['Nome']}: '))

print(f'O nome do aluno(a) é {escola['Nome']}')
print(f'A sua média é {escola['Media']}')

if escola['Media'] >= 6:
    print('Situação é igual a aprovado')
else:
    print('Situação é igual a reprovado')
