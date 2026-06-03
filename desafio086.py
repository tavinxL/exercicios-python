somapar = 0
somac = 0
maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f'Digite os valores para [{l}, {c}]: '))
        if matriz[l] [c] % 2 == 0:
            somapar = somapar + matriz[l] [c]
        else:
            if c == 2:
                somac = somac + matriz[l] [c]
            if l == 1:
                maior = matriz[l] [c]
                if matriz[l] [c] > maior:
                    maior = matriz[l] [c]





for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
    print()

print(f'As soma dos valores pares da matrix é {somapar}')
print(f'A soma da coluna 3 é {somac}')
print(f'O maior valor da segunda linha é {maior}')

