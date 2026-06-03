print('~'*30)
print('   VARIOS NÚMEROS COM FLAG')
print('~'*30)

num = 0
soma = 0
c = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    c += 1
print(f'Foram digitados {c} valores')
print(f'A soma entre os números, desconsiderando o número 999, é igual a {soma}')

