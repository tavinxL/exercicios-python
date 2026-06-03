print('~'*30)
print('    PROGRESSÃO ARITMÉTICA    ')
print('~'*30)

p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão dessa PA: '))
termos = int(input('Quantos termos você deseja saber ?: '))
n = 1
print()

while n <= termos:
    an = p1 + (n - 1) * r
    print(f'Termo {n} = {an}')
    n += 1
print()

termos = int(input('Você quer ver mais termos ? Se sim, digite quantos, se não, digite 0: '))
print()
while termos != 0:
    if termos != 0:
        an = p1 + (n - 1) * r
        print(f'Termo {n} = {an}')
        n += 1
        termos -= 1
        if termos == 0:
            print()
            termos = int(input('Você quer ver mais termos ? Se sim, digite quantos, se não, digite 0: '))
            print()

print('FIM')
