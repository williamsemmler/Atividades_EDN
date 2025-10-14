'''  4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia. '''

import datetime

print("=" * 6, "Dias vivo!", "=" * 6, sep= " ")

dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))

dataNascimento = datetime.datetime(ano, mes, dia)
timestamp_dataNascimento = int(dataNascimento.timestamp())

data_hora_atual = datetime.datetime.now()
timestamp_atual = int(data_hora_atual.timestamp())

tempo_de_vida = timestamp_atual - timestamp_dataNascimento

tempo_de_vida_em_dias = tempo_de_vida / 60 / 60 / 24

print(f"Este individual está vivo a {tempo_de_vida_em_dias:.0f} dias ou aproximadamente {(tempo_de_vida_em_dias/365):.2f} anos")


print("=" * 6, "Fim do Programa", "=" * 6, sep= " ")