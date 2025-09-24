# 3- Calculadora de Volume
# * Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:
# * Comprimento: 12 cm
# * Largura: 14 cm
# * Altura: 20 cm
# O programa deve calcular o volume e exibir o resultado em cm³.
# fórmula: Volume = Comprimento × Largura × Altura

print("=" * 6, "Calculadora de volumes", "=" * 6, sep= " ")

c = 12
l = 14
a = 20

def calculaVolumeRetangulo(comp, larg, alt):
    volume = comp * larg * alt
    return volume

volumeRetangulo = calculaVolumeRetangulo(c, l, a)

print(f'O volume do retângulo é de {volumeRetangulo:.2f}m³')
print("=" * 6, "Fim do programa", "=" * 6, sep= " ")