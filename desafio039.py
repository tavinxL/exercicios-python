print('---ALISTAMENTO MILITAR---')

idade = int(input('Digite sua idade: '))
faltam = 18 - idade
prazo = idade - 18

if idade < 18 and faltam > 1:
    print('Voce ainda nao tem a idade adequada para se alistar, ainda faltam {}{}{} anos' .format('\033[31m', faltam, '\033[m'))
elif idade < 18 and faltam == 1:
    print('Voce ainda nao tem a idade adequada para se alistar, ainda falta {}{}{} ano'.format('\033[34m' ,faltam, '\033[m'))

elif idade == 18:
    print('Você ja tem a idade adequada para se alistar')

elif idade > 18 and prazo > 1:
    print('Você passou {}{}{} anos da idade correta de se alistar' .format('\033[35m' ,prazo, '\033[m'))

else:
    print('Você passou {}{}{} ano da idade correta de se alistar'.format('\033[36m' ,prazo, '\033[m'))

print('---FIM---')
