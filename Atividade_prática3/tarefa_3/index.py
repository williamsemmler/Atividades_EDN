'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

print("=" * 6, "Conversor de Temperatura", "=" * 6, sep=" ")

temperatura = float(input("Digite a temperatura: "))
print("Selecione a temperatura de origem:\n 1: Celsius\n 2: Fahrenheit\n 3: Kelvin")
unidOrigem = int(input("> "))

print("Selecione a temperatura de destino:\n 1: Celsius\n 2: Fahrenheit\n 3: Kelvin")
unidConv = int(input("> "))

def conversaoTemp(temp, undOrigem, undDestino):
    if undOrigem == 1 and undDestino == 2:
        tempConvertida = (1.8 * temp) + 32
        print(f'A conversão de {temp} °C para Fahrenheit é {tempConvertida:.2f} °F')
    elif undOrigem == 2 and undDestino == 1:
        tempConvertida = (temp - 32) / 1.8
        print(f'A conversão de {temp} °F para Celsius é {tempConvertida:.2f} °C')
    elif undOrigem == 1 and undDestino == 3:
        tempConvertida = temp + 273.15
        print(f'A conversão de {temp} °C para Kelvin é {tempConvertida:.2f} K')
    elif undOrigem == 3 and undDestino == 1:
        tempConvertida = temp - 273.15
        print(f'A conversão de {temp} K para Celsius é {tempConvertida:.2f} °C')
    elif undOrigem == 2 and undDestino == 3:
        tempConvertida = (temp - 32) * 5/9 + 273.15
        print(f'A conversão de {temp} °F para Kelvin é {tempConvertida:.2f} K')
    elif undOrigem == 3 and undDestino == 2:
        tempConvertida = (temp - 273.15) * 1.8 + 32
        print(f'A conversão de {temp} K para Fahrenheit é {tempConvertida:.2f} °F')
    else:
        print("Opção inválida!")

conversaoTemp(temperatura, unidOrigem, unidConv)
