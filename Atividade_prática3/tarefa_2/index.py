'''2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
fórmula -> IMC = Peso (kg) / (Altura (m) x Altura (m))'''


print("=" * 6, "Calculadora de IMC", "=" * 6, sep= " ")
inputPeso = float(input("Digite seu peso em quilogramas: "))
inputAltura = float(input("Digite sua altura em metros: "))

def calculaImc(peso, altura):
    imc = peso/(altura * altura)
    
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 24.9:
        print("Classificação: Peso normal")
    elif imc < 29.9:
        print("Classificação: Sobrepeso")
    elif imc >= 30:
        print("Classificação: Obesidade")
        
calculaImc(inputPeso, inputAltura)