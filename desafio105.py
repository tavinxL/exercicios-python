def notas(*n, sit=False):
    """
    Função para analisar notas e situações de vários alunos
    :param n: Receber as notas dos alunos (aceita várias)
    :param sit: Valor opcional para ver ou não a situação do aluno
    :return: Dicionário com varias informações sobre a situação do aluno
    """
    totnotas = maior = menor = cont = media = 0
    totnotas = len(n)
    for valor in n:
        if cont == 0:
            maior = menor = valor
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
        cont += 1
    media = sum(n) / len(n)

    dicnotas = {'total': totnotas, 'maior': maior, 'menor': menor, 'media': media}

    if sit:
        if media >= 6:
            dicnotas['situação'] = 'BOA'
        else:
            dicnotas['situação'] = 'RUIM'
    return dicnotas



resp = notas( 7.2, 8.4, 1.9, sit=True)
print(resp)
help(notas)





