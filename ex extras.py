senha = 'melancia'

print(f'Tem pelo menos 8 caracteres? {len(senha) >= 8}')
print(f'Na senha, tem números ? {any(c.isdigit() for c in senha)}')
print(f'Na senha, tem letras maiusculas ? {any(c.isupper() for c in senha)}')

valida = len(senha) >= 8 and any(c.isdigit() for c in senha) and any(c.isupper() for c in senha)
print(f'Senha válida? {valida}')