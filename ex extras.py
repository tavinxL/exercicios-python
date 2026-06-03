dicionario = {}
frase = input('Digite um frase: ').split()
for c in frase:
    if c in dicionario:
        dicionario[c] += 1
    else:
        dicionario[c] = 1

print(dicionario)





