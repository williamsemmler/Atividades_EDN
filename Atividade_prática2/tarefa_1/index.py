''' 1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais. '''

print("=" * 6, "Conversor de Moedas", "=" * 6, sep= " ")

real = float(input("Digite o valor em real: "))
txDolar = 5.20
txEuro = 6.15

convDolar = real / txDolar
convEuro = real / txEuro

print(f'O valor de R$ {real:.2f} convertido para Dólar é de R$ {convDolar:.2f} e para Euro é de R$ {convEuro:.2f}')

print("=" * 6, "Fim do programa", "=" * 6, sep= " ")
