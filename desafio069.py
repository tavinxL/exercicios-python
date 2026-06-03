from time import sleep

print("="*30)
print('Analise de dados')
print("="*30)

p = 'S'
soma18 = 0
somamasculino = 0
somafemidade = 0
while True:
    sexo = input('Digite seu sexo [M/F]: ').upper().strip()[0]
    idade = int(input('Digite sua idade: '))
    sleep(1)
    print('Pessoa cadastrada, aguarde um instante...')
    sleep(1)

    if idade > 18:
        soma18 += 1
    if sexo == 'M':
        somamasculino += 1
    if sexo == 'F' and idade < 20:
        somafemidade += 1

    p = input('Voce deseja continuar [S/N]: ').upper().strip()[0]
    if p == 'N':
        break

print(f'No final, foram cadastrados {soma18} pessoas com mais de 18 anos\n{somamasculino} pessoas homens\n{somafemidade} mulheres com menos de 20 anos')
