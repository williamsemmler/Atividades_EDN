# 4- Calculadora de Preço Total
# * Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:
# * Nome do produto: "Cadeira Infantil"
# * Preço unitário: R$ 12.40
# * Quantidade: 3
# O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

print("=" * 6, "Cálculo de preço total", "=" * 6, sep= " ")

lista_itens = [
    {
        "nomeProduto": "Cadeira infantil",
        "precoUnitario": 12.40,
        "quantidade": 3
    },
    {
        "nomeProduto": "Bicicleta",
        "precoUnitario": 1200.00,
        "quantidade": 5
    }
]

def calculaPrecoTotal(item, numero):
    precoTotalProduto = item[numero]["precoUnitario"] * item[numero]["quantidade"]
    print('Informações do produto:')
    print(f'- Nome do produto: {item[numero]["nomeProduto"]}')
    print(f'- Preço unitário: R$ {item[numero]["precoUnitario"]:.2f}')
    print(f'- Quantidade: {item[numero]["quantidade"]}')
    print(f'- Preço total: R$ {precoTotalProduto:.2f}')
    print("\n")


cadeiraInfantil = calculaPrecoTotal(lista_itens, 0)
bicicleta = calculaPrecoTotal(lista_itens, 1)
