print('---APROVAÇÃO EMPRESTIMO---')

valorcasa = float(input('Qual o valor da casa que você deseja comprar ?: '))
salario = float(input('Qual é o seu salário ?: '))
parcelasano = int(input('Em quantos anos você deseja pagar ?: '))
pm = parcelasano * 12
prestacaomensal = valorcasa / pm
excedente = float(salario * 0.3)

print('O valor que você ira pagar por mês é de {:.2f}' .format(prestacaomensal))
if prestacaomensal < excedente:
    print('Você esta dentro das normas e vai conseguir realizar o emprestimo')
else:
    print('Voce nao pode realizar o emprestimo, pois o valor da prestação excedeu 30% do seu salário')



