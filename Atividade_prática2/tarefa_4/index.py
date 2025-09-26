'''4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.'''


print("=" * 6, "Calculadora de Consumo de Combustível", "=" * 6, sep= " ")

distPercorrida = 300
combustivelGasto = 25
kmPorLitro = distPercorrida/combustivelGasto

print("Dados de consumo:")
print(f' - Distância percorrida: {distPercorrida}km\n - Combustível gasto: {combustivelGasto}lts\n - Km/litros: {kmPorLitro:.2f}')

print("=" * 6, "Fim do programa", "=" * 6, sep= " ")