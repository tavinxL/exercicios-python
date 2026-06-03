num = 0
c = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    print()
    if num != 999:
        soma += num
        c += 1
print(f'Foi digitado {c} números!')
print(f'A soma dos números digitados, tirando o número 999, é {soma}')

