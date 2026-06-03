c = 0
lista = []

n = int(input('Digite um número: '))
lista.append(n)
print('Adicionando ao final da lista')

while c < 5:
    c += 1
    n = int(input('Digite um número: '))


    if n in lista:
        print('Número já existe na lista, ignorando.')
        continue


    posicao = len(lista)
    for i in range(len(lista)):
        if n < lista[i]:
            posicao = i
            break

    lista.insert(posicao, n)
    print(f'Adicionando na posição {posicao}')

print(lista)