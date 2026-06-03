print('===PA===')
print()

p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão dessa PA: '))
for n in range(1, 11):
    an = p1 + (n - 1) * r
    print('Termo {} = {}' .format(n, an))
print('===FIM===')
