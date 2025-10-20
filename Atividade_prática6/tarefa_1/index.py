''' 1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.'''

print("=" * 6, "Gerador de senhas aleatórias", "=" * 6, sep= " ")

import random
import string

print("Gerador de senhas")

tamanho = int(input("Digite o tamanho da senha: "))

letras = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation

tudo = letras + numeros + simbolos

senha = ""

for i in range(tamanho):
    senha += random.choice(tudo)

print("Senha gerada:", senha)


print("=" * 6, "Fim do Programa", "=" * 6, sep= " ")