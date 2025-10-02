'''4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.'''


print("=" * 6, "Verificador de ano bissexto", "=" * 6, sep= " ")

try:
    anoBase = int(input("Digite um ano qualquer: "))
    anoBissexto = "Ano bissexto" if (anoBase % 4 == 0 and anoBase % 100 != 0) or (anoBase % 400) else "Ano não bissexto"
    print(anoBissexto)
except:
    print("Ano incorreto")