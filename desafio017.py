import math
co = int(input('Qual o comprimento do Cateto Oposto ?: '))
ca = int(input('Qual o comprimento do Cateto Adjacente ?: '))
hi = math.hypot(co, ca)
a = math.trunc(hi)
print('A hipotenusa de {} e {} é {}' .format(co, ca, a))


