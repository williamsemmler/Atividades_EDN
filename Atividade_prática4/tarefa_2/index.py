'''2- Criar um código que registre as notas de alunos e calcular a média da turma'''


print("=" * 6, "Média da turma", "=" * 6, sep= " ")

notas_turma = []
while True:
    nota = float(input("Digite a nota dos alunos (Digite '-1' para encerrar a operação): "))
    if nota == -1:
        break
    notas_turma.append(nota)
    
print(notas_turma)

notas_consolidadas = 0
for nota in notas_turma:
    notas_consolidadas += nota

media_geral = notas_consolidadas / len(notas_turma)

print(f'A média das notas informadas é {media_geral:.2f}')

print("=" * 6, "Fim do Programa", "=" * 6, sep= " ")
