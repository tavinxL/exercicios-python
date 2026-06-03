num = int(input('Digite qualquer número: '))
print('''Escolha para qual base você deseja converter:
[ 1 ] - binário
[ 2 ] - octal
[ 3 ] - hexadecimal''')
basecon = int(input())

b = (bin(num)[2:])
o = (oct(num)[2:])
h = (hex(num)[2:])

if basecon == 1:
    print('CONVERTENDO...')
    print('O numero {} convertido para a base binária é {}'. format(basecon, b))
elif basecon == 2:
    print('CONVERTENDO...')
    print('O número {} convertido para base octal é {}' .format(basecon, o))
else:
    print('CONVERTENDO...')
    print('O número {} convertido para a base hexadecimal é {}' .format(basecon, h))