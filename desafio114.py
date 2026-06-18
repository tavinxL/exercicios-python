import requests

def verificarurl(url):
    try:
        resposta = requests.get(url)
        if resposta.ok:
            print(f'O site {url} está funcionando!')
    except requests.ConnectionError:
        print(f'Erro: O site {url} não esta disponivel no momento')

verificarurl("https://google.com")
