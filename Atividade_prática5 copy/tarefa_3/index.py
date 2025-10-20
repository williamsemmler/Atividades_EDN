''' 3 - Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha. '''

print("=" * 6, "Busca CEP", "=" * 6, sep= " ")

import requests

print("Consulta de CEP")

cep = input("Digite o CEP (somente números): ")

try:
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if resposta.status_code == 200:
        dados = resposta.json()

        if "erro" not in dados:
            print("Logradouro:", dados["logradouro"])
            print("Bairro:", dados["bairro"])
            print("Cidade:", dados["localidade"])
            print("Estado:", dados["uf"])
        else:
            print("CEP não encontrado.")
    else:
        print("Falha na requisição.")
except:
    print("Erro de conexão. Tente novamente.")
    
    
    
print("=" * 6, "Fim do Programa", "=" * 6, sep= " ")