lista = []
expressao = input('Digite uma expressão: ')
lista.append(expressao)

a = expressao.count('(')
b = expressao.count(')')

if a % 2 == 0 and b % 2 == 0:
    print('Expressão valida')
else:
    print('Expressão inválida')
