def voto(anonascimento):
    idade = 2026 - anonascimento
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'




votacao = voto(int(input('Em que ano você nasceu ?: ')))
print(votacao)
