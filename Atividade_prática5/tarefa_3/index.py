''' 3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado. '''

print("=" * 6, "Preço final do produto", "=" * 6, sep= " ")

valorTotal = float(input("Digite o valor do produto: "))
descontoPretendido = float(input("Digite o percentual de desconto pretendido: "))

def calculaDesconto(preco, desconto):
    return preco * (desconto / 100)

desconto = calculaDesconto(valorTotal, descontoPretendido)

print()
print(f" - Preço total: R$ {valorTotal:.2f}")
print(f" - Desconto percentual: {descontoPretendido:.2f}%")
print(f" - Valor desconto: R$ {desconto:.2f}")
print(f" - Valor final do produto: R$ {(valorTotal - desconto):.2f}")

print()
print("=" * 6, "Fim do Programa", "=" * 6, sep= " ")