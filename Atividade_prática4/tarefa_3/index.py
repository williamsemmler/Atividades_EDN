'''3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.'''

print("=" * 6, "Verificador de senhas", "=" * 6, sep=" ")


while True:
    print("Digite uma senha")
    senhaDigitada = input("senha (mínimo de 8 caracteres e mínimo de 1 número): ")

    oitoDigitos = len(senhaDigitada)
    letra = []
    numero  = []
    if oitoDigitos >= 8:
        for digito in senhaDigitada:
            digitoValidacao = digito.isdigit()
            if digitoValidacao == True:
                numero.append("true")
            elif digitoValidacao == False:
                letra.append("false")
    else:
        print("Senha menor de 8 caracteres, tente novamente")
        continue

    if len(letra) == 0 or len(numero) == 0:
        print()
        print("Senha não atendeu ao requisito. Favor escrever uma senha correta")
        continue
    else:
        print()
        print("A senha atendeu aos requisitos")
        print("=" * 6, "Fim do Programa", "=" * 6, sep= " ")
        break