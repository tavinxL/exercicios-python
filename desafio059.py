from time import sleep

print('~'*15)
print('MENU DE OPÇÕES')
print('~'*15)

escolha = 0

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while escolha != 5:
    print('''[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior valor\n[ 4 ] Novos números\n[ 5 ] Sair''')
    escolha = int(input('Escolha uma opção: '))
    print()

    if escolha == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é igual a {soma}')
        print()
    elif escolha == 2:
        multiplicar = num1 * num2
        print(f'A multiplicação entre {num1} e {num2} é igual a {multiplicar} ')
        print()
    elif escolha == 3:
        if num1 > num2:
            print(f'O maior valor é o {num1}')
            print()
        else:
            print(f'O maior valor é o {num2}')
            print()
    elif escolha == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    elif escolha > 5:
        print('OPÇÃO INVÁLIDA, ESCOLHA NOVAMENTE!!!')
print('SAINDO...')
sleep(1)



