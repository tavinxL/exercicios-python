from time import sleep

from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'arquivosistema.txt'

if arqexiste(arq):
    print('Arquivo encontrado com sucesso')
else:
    print('Arquivo não encontrado')
    criaraquivo(arq)

while True:
    resposta = menu(['Listas todas as pessoas','Cadastrar novas pessoas','Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        # Opção 2 cadastra novas pessoas
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema, até logo...')
        break
    else:
        print('\033[0;31mERRO! Digite uma opcao valida\033[m')
    sleep(2)
