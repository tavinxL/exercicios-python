print('---AUMENTO SALARIAL---')
sa = float(input('Qual é o seu salario atual ?: '))
if sa > 1250:
    print('Seu salario terá um aumento de 10%')
    sf = sa * 1.10
    print('Seu salario com o aumento é de {:.2f}'.format(sf))
else:
    print('Seu salário tera um aumento de 15%')
    sf = sa * 1.15
    print('Seu salário com o aumento é de {:.2f}' .format(sf))
print('---FIM---')
