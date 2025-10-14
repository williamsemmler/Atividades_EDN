''' 1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada '''

print("=" * 6, "Cálculo de gorjeta", "=" * 6, sep= " ")

totalConta = float(input("Digite o valor total da conta: "))
porcentagemGorjeta = float(input("Digite o percentual de gorjeta desejado: "))

def calculaGorjeta (total, percentual):
    return total * (percentual / 100)

valorGorjeta = calculaGorjeta(totalConta, porcentagemGorjeta)

print(f"Valor total da conta: R$ {totalConta:.2f}")
print(f"Percentual de gorjeta: {porcentagemGorjeta:.2f}%")
print(f"Total gorjeta: R$ {valorGorjeta:.2f}")
print(f"Total final da conta: R$ {(totalConta + valorGorjeta):.2f}")


print("=" * 6, "Fim do Programa", "=" * 6, sep= " ")