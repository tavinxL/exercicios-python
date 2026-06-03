print('===ANALISANDO ATLETAS===')
print()

anon = int(input('Qual é o seu ano de nascimento ?:'))
idade = 2026 - anon
print()

if idade <= 9:
    print('IDADE: {} ANOS' .format(idade))
    print('MIRIM')

elif 9 < idade <= 14:
    print('IDADE: {} ANOS'.format(idade))
    print('INFANTIL')

elif 14 < idade <= 19:
    print('IDADE: {} ANOS'.format(idade))
    print('JUNIOR')

elif 19 < idade <= 20:
    print('IDADE: {} ANOS'.format(idade))
    print('SÊNIOR')

else:
    print('IDADE: {} ANOS'.format(idade))
    print('MASTER')