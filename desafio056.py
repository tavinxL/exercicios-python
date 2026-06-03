print('===ANALISADOR COMPLETO===')
print()

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for c in range(1, 5):
    nome = input(f'Qual o nome da {c} pessoa ?: ')
    idade= int(input(f'Qual é a idade da {c} pessoa ?: '))
    sexo = input(f'Qual é o sexo da {c} pessoa ? [M/F]: ')
    print()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4

print(f'A média de idade do grupo é de {mediaidade:.1f}')
print(f'O homem mais velho tem {maioridadehomem}, e seu nome é {nomevelho}')
print(f'Ao todo, são {totmulher} mulher(es) que possuem menos de 20 anos de idade')










