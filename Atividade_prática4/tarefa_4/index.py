'''4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.'''


print("=" * 6, "Separador de pares e ímpares", "=" * 6, sep= " ")

pares = []
impares = []
countPares = 0
countImpares = 0
while True:
    numero = input("Digite um número (digite uma letra para finalizar a operação): ")
    try:
        numeroInt = int(numero)
        
        if numeroInt % 2 == 0:
            pares.append(numeroInt)
            countPares += 1
        else:
            impares.append(numeroInt)
            countImpares += 1
    except:
        print("Fim do programa")
        break

print(f'Total de números pares: {countPares} - {pares}')
print(f'Total de números ímpares: {countImpares} - {impares}')

print()
print("=" * 6, "Fim do Programa", "=" * 6, sep= " ")
