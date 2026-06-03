print()
print('{:=^50}'.format('GERENCIADOR DE PAGAMENTOS'))

preco = float(input('Qual é o valor do produto ?: '))
print()
print('''Qual será a forma de pagamento ?:\n [ 1 ] - Dinheiro/Cheque\n [ 2 ] - Débito\n [ 3 ] - 1x no Cartão\n [ 4 ] - 2x no cartão\n [ 5 ] - 3x ou mais no cartão''')
formap = int(input('Escolha uma opção: '))
print()

if formap == 1:
    des = float(0.90)
    total = preco * des
    print('Como você escolheu pagar em dinheiro/cheque, vamos dar 10% de desconto\n Então o total sai de R${:.2f} para R${:.2f}' .format(preco, total))

elif formap == 2:
    des = float(0.95)
    total = preco * des
    print('Como você escolheu pagar no débito, vamos dar 5% de desconto\n Então o total sai de R${:.2f} para R${:.2f}' .format(preco, total))

elif formap == 3:
    print('Nessa forma de pagamento não damos desconto, você irá pagar em 1x de R${:.2f}' .format(preco))

elif formap == 4:
    totparc = preco / 2
    print('Nessa forma de pagamento não damos desconto, você irá pagar em 2x de R${:.2f}, que no total da {:.2f}'.format(totparc, preco))

else:
    parcelas = int(input('Em quantas parcelas você deseja fazer ?: '))
    juros = float(1.20)
    total = preco * juros
    preparc = preco / parcelas
    totparc = total / parcelas
    print('Nessa forma de pagamento, vai ter um juros de 20%\nSaindo de {}x de R${:.2f}, que daria R${:.2f} para {}x de R${:.2f} que dá R${:.2f}' .format(parcelas, preparc, preco, parcelas, totparc, total))

print('{:=^40}' .format('FIM'))



















