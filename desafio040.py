print('---MÉDIA---')
print()

not1 = float(input('Digite sua primeira nota: '))
not2 = float(input('Digite sua segunda nota: '))
m = (not1 + not2) / 2
print()

if m < 5.0:
    print('REPROVADO')
    print('Você ficou com {} de média' .format(m))

elif 5.0 < m < 7.0:
    print('RECUPERAÇÃO')
    print('Você ficou com {} de média'.format(m))

else:
    print('APROVADO')
    print('Você ficou com {} de média'.format(m))
