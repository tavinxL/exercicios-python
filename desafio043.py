print('===CÁLCULO IMC===')
print()

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / altura ** 2
print()

if imc < 18.5:
    print('Seu imc é de {:.1f}' .format(imc))
    print('Você esta abaixo do peso')

elif 18.5 <= imc < 25:
    print('Seu imc é de {:.1f}'.format(imc))
    print('Você esta no peso ideal')

elif 25 <= imc < 30:
    print('Seu imc é de {:.1f}'.format(imc))
    print('Você esta em sobrepeso')

elif 30 <= imc < 40:
    print('Seu imc é de {:.1f}'.format(imc))
    print('Você esta com obesidade')

else:
    print('Seu imc é de {:.1f}'.format(imc))
    print('Você esta com obesidade mórbida')
