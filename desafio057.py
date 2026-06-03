print('~'*30)
print('MASCULINO OU FEMININO')
print('~'*30)

sexo = input('Digite seu sexo [M/F]: ').upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input('Por favor, digite seu sexo corretamente: ').upper().strip()[0]
print(f'Seu sexo é {sexo}')