print('---PAR OU ÍMPAR---')
num = int(input('Digite um número: '))
print('O número digitado foi {}' .format(num))
poi = num % 2
if poi == 0:
    print('O número digitado é par')
else:
    print('O numero digitado é impar')
print('---FIM---')