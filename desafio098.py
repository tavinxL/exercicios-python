from time import sleep


def contador(inicio, fim, passo):
    print('~'*40)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            sleep(0.5)
            print(cont, end=' ', flush=True)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            sleep(0.5)
            print(cont, end=' ', flush=True)
            cont -= passo
        print('FIM!')
        print('~' * 40)

contador(1, 10, 1)
contador(10, 0, 2)


print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
final = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, final, pas)




