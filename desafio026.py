fr = input('Escreva uma frase qualquer: ').upper().strip()
print('Nesta frase, a letra A aparece {}' .format(fr.count('A')))
print('A letra A aparece pela primeira vez na posição {}' .format(fr.find("A")+1))
print('A letra A aparece pela ultima vez na posição {}' .format(fr.rfind('A')+1))