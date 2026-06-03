print('='*30)
print('{:^30}' .format('Numeros por extenso'))
print('='*30)

cont = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
        'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


while True:
    valor = int(input('Digite um número: '))
    if 0 <= valor <= 20:
        break
    print('Tente Novamente. ', end='')
print(f'Voce digitou o número {cont[valor]}')
