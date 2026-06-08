def area(* num):
    print(f'A área tem um tamanho de {num[0]}m², no qual, o comprimento tem valor {num[1]}m e a largura valor {num[2]}m')

largura = float(input('LARGURA (M): '))
comprimento = float(input('COMPRIMENTO (M): '))
calculo = largura * comprimento
area(calculo, comprimento, largura)



