print('---CUSTO DA VIAGEM---')
d = float(input('Qual a distância da viagem ?: '))
print('A distância da sua viagem é de {} Km' .format(d))
if d <= 200:
    pas = 0.5 * d
    print('O preço da sua passagem é de {} reais' .format(pas))
else:
    pas = 0.45 * d
    print('O preço da sua passagem é de {} reais' .format(pas))
print('---FIM---')
