''' 1- Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/). '''

print("=" * 6, "Calculadora", "=" * 6, sep= " ")

while True:
    numeros = []
    valor1 = input("Digite um número: ")
    try:
        valorFloat = float(valor1)
        numeros.append(valorFloat)
        valor2 = input ("Digite o segundo valor:" )
        try:
            valor2Float = float(valor2)
            numeros.append(valor2Float)
            break
        except:
            print("Não foi possível realizar a conversão do valor. Insira um valor válido.")
            continue
    except:
        print("Não foi possível realizar a conversão do valor. Insira um valor válido.")
        continue

print("Operação matemática")
while True:
    operacao = int(input(" 1. Soma\n 2. Subtração\n 3. Divisão\n 4. Multiplicação\n> "))
    if operacao < 1 or operacao > 4:
        print("Não é um valor válido, digite uma operação entre 1 e 4")
        continue
    else:
        break


def calcular(arrayNumeros, operacaoMat):
    numeros = arrayNumeros
    operacao = operacaoMat
    
    if operacao == 1:
        return numeros[0] + numeros[1]
    elif operacao == 2:
        return numeros[0] - numeros[1]
    elif operacao == 3:
        return numeros[0] / numeros[1]
    else:
        return numeros[0] * numeros[1]

resultado = calcular(numeros, operacao)
print(f'O resultado da operação é: {resultado:.2f}')

print("=" * 6, "Fim do Programa", "=" * 6, sep= " ")