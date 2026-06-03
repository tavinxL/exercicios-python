print('TABUADA V2')
n = int(input('Digite qual o número você deseja saber a tabuada: '))
for c in range(0, 11):
    t = n * c
    print('{} x {} = {}' .format(n, c, t))
print('FIM')
