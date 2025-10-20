'''  4 - Crie um programa que realize consultas a em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro. '''

import requests

print("Consulta de câmbio")

moeda = input("Digite a sigla da moeda (ex: USD, EUR): ").upper()

try:
    resposta = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL")
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"

        if chave in dados:
            info = dados[chave]
            print("Moeda:", info["code"])
            print("Valor atual:", info["bid"])
            print("Máxima:", info["high"])
            print("Mínima:", info["low"])
            print("Última atualização:", info["create_date"])
        else:
            print("Moeda não encontrada.")
    else:
        print("Falha na requisição.")
except:
    print("Erro de conexão. Tente novamente.")


print("=" * 6, "Fim do Programa", "=" * 6, sep= " ")