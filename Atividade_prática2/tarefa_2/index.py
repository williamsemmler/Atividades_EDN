'''2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.'''


print("=" * 6, "Calculadora de Descontos", "=" * 6, sep= " ")

nomeProduto = "Camiseta"
preco = 50.00
descontoPercent = 20

def calculaDesconto(preco, desconto):
    valorDesconto = preco * (desconto / 100)
    return valorDesconto

descontoCamiseta = calculaDesconto(preco, descontoPercent)
valorFinalCamiseta = preco - descontoCamiseta

print("=" *6, "Dados finais", "=" * 6, sep=" ")
print(f'Produto: {nomeProduto}\nPreço original: R$ {preco:.2f}\nPercentual de Desconto: {descontoPercent:.2f}%\nValor do desconto: R$ {descontoCamiseta:.2f}\nProduto com desconto: R$ {valorFinalCamiseta:.2f}')

print("=" * 6, "Fim do programa", "=" * 6, sep= " ")
