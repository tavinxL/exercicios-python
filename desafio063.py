t1 = 0
t2 = 1
t3 = 0
c = 3
print('~'*23)
print('SEQUÊNCIA DE FIBONACCI')
print('~'*23)

num = int(input('Quantos termos você quer saber ?: '))
print('~'*23)
print(f'{t1} -> {t2}', end='')
while c <= num:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    c += 1

