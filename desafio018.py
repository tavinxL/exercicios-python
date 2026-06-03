import math
a = float(input('Digite um angulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O angulo {} tem valor seno de {:.2f}' .format(a, s))
print('O angulo {} tem valor cosseno de {:.2f}' .format(a, c))
print('O angulo {} tem valor tangente de {:.2f}' .format(a, t))
