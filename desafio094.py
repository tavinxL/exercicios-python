pessoas = dict()
dados = list()
listamulheres = list()
pessoascadastradas = 0
media = totidade = 0
pessoas_acimamedia = list()

while True:
    pessoas.clear()
    nome = input('Qual é o seu nome ?: ')
    pessoas['Nome'] = nome

    idade = int(input('Qual é a sua idade ?: '))
    totidade = totidade + idade
    pessoas['Idade'] = idade

    sexo = input('Qual é o seu sexo ? [M/F]:  ').upper().strip()[0]
    if sexo == 'F':
        listamulheres.append(nome)
    pessoas['Sexo'] = sexo

    pessoascadastradas += 1
    dados.append(pessoas.copy())

    r = input('Você deseja adicionar mais alguem ? [S/N]: ').upper().strip()[0]
    if r not in 'Ss':
        break

print('=-'*30)
print(f'Ao todo, foram cadastradas {pessoascadastradas} pessoas')

media = totidade / len(dados)
print(f'A media de idade do grupo é de {media:.2f}')

print(f'As mulheres cadastradas na lista é {listamulheres}')

for p in dados:
    if p['Idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}', end=' / ')
        print()









