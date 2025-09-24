# 2- Calculadora de Soma
# * Desenvolva um programa que soma dois números. Use as variáveis numero1 = 12 e numero2 = 14. O programa deve calcular a soma e exibir o resultado.

print("=" * 6, "Programa iniciado", "=" * 6, sep= " ")
numero1 = 12
numero2 = 14

def somaValores(x, y):
    print(f'A soma dos valores {x} e {y} é de {x + y}')

somaValores(numero1, numero2)
print("=" * 6, "Fim do programa", "=" * 6, sep= " ")