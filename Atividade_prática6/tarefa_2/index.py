''' 2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha. '''

print("=" * 6, "Usuário fictício", "=" * 6, sep= " ")

import requests

print("Buscando usuário aleatório...")

try:
    resposta = requests.get("https://randomuser.me/api/")
    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados["results"][0]

        nome = usuario["name"]["first"] + " " + usuario["name"]["last"]
        email = usuario["email"]
        pais = usuario["location"]["country"]

        print("Nome:", nome)
        print("E-mail:", email)
        print("País:", pais)
    else:
        print("Falha ao buscar o usuário.")
except:
    print("Erro de conexão. Tente novamente.")



print("=" * 6, "Fim do Programa", "=" * 6, sep= " ")