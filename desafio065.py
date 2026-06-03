pergunta = 'S'
num = 0
c = 0
soma = 0
while pergunta == 'S':
    num = int(input('Digite um número: '))
    pergunta = input('Você deseja continuar [S/N] ? ').upper().strip()
    c += 1
    soma += num
    media = soma / c
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    if pergunta == 'N':
        print(f'A media de todos os valores somados é igual a {media:.2f}')
        print(f'O maior valor digitado foi {maior}')
        print(f'O menor valor digitado foi {menor}')

