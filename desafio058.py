import random

c = 1
palpites = 0
ec = random.randint(0, 10)
print('O COMPUTADOR PENSOU EM UM NÚMERO...')
eu = int(input('Advinhe qual numero o computador pensou entre 0 e 10: '))
while eu != ec:
    c += 1
    print(ec)
    if eu < ec:
        eu = int(input('MAIS... TENTE OUTRA VEZ: '))

    else:
        eu = int(input('MENOS... TENTE OUTRA VEZ: '))

print('Você advinhou, parabens!')
palpites += c
print(f'Para você acertar, você tentou {palpites} vezes')

