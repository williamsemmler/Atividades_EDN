''' 2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”. '''

print("=" * 6, "É Palindromo?", "=" * 6, sep= " ")

palavra = str(input("Digite uma palavra para verificar se é palíndromo: ")).lower()

novaPalavra = []
for letra in palavra:
    novaPalavra.insert(0, letra)

separator = ''
palavraInvertida = separator.join(novaPalavra)

if palavra == palavraInvertida:
    print("É palíndromo")
else:
    print("Não é palíndromo")    


print("=" * 6, "Fim do Programa", "=" * 6, sep= " ")