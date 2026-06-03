
print('='*30)
print('Estatisticas de Produtos')
print('='*30)


totalgasto = 0
produtos1000 = 0
barato = ''
menor = 0
cont = 0
while True:
    nomeproduto = input('Qual é o nome do produto: ')
    precoproduto = float(input('Qual o preço do produto: R$'))
    totalgasto += precoproduto
    cont += 1

    if precoproduto > 1000:
        produtos1000 += 1

    if cont == 1 or precoproduto < menor:
        menor = precoproduto
        barato = nomeproduto

    continuar = input('Voce deseja adicionar outro produto ? [S/N]: ').upper().strip()[0]
    if continuar != 'S':
        break

print(f'O total gasto foi de {totalgasto :.2f}, {produtos1000} produto(s) que custam acima de R$1000, e o produto mais barato foi o {barato} que custa R${menor} reais')









