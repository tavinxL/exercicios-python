from datetime import datetime

trabalhador = dict()

trabalhador['Nome'] = input('Nome: ')
trabalhador['AnoNascimento'] = int(input('Ano de nascimento: '))
trabalhador['CarteiraTrabalho'] = int(input('Carteira de Trabalho (0 nao tem): '))
if trabalhador['CarteiraTrabalho'] != 0:
    trabalhador['Idade'] = datetime.now().year - trabalhador['AnoNascimento']
    trabalhador['AnoContratacao'] = int(input('Ano de contratação: '))
    trabalhador['Salario'] = float(input('Salario: '))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + ((trabalhador['AnoContratacao'] + 35) - datetime.now().year)

print()

for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')