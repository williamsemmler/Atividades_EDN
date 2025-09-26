'''3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.'''

import statistics as st

print("=" * 6, "Calculadora de Média Escolar", "=" * 6, sep= " ")
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

notas = [nota1, nota2, nota3]
mediaNotas = st.mean(notas)

print(f'Notas:\n - Nota 1: {nota1:.2f}\n - Nota 2: {nota2:.2f}\n - Nota 3: {nota3:.2f}')
print(f'Média final: {mediaNotas:.2f}')

print("=" * 6, "Fim do programa", "=" * 6, sep= " ")
