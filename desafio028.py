import random

escolhas = [0, 1 ,2, 3, 4, 5]
eu = int(input('Advinhe qual numero o computador ira escolher entre 0 e 5: '))
ec = random.choice(escolhas)
print('O numero escolhido pelo computador foi {}' .format(ec))
print('O usuario escolheu o numero {}' .format(eu))

if eu == ec:
    print('Você advinhou, parabens!')
else:
    print('Você errou, tente novamente')