print('---RADAR ELETRONICO---')
vel = float(input('Qual a velocidade do carro ?: '))
velm = 80
print('A velocidade máxima é de {} Km/h' .format(velm))
print('Sua velocidade era de {} Km/h' .format(vel))
if vel > 80:
    kma = vel - velm
    multa = kma * 7
    print('Voce irá tomar uma multa de {} reais, pois voce estava {} Km/h acima do permitido' .format(multa, kma))
else:
    print('Voce estava dentro da velocidade permitida')
print('---FIM---')
