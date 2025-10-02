''' 1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais). '''

print("=" * 6, "Classificador de Idade", "=" * 6, sep= " ")


position = 0
lista = []


def adicionaNaLista(position, idade):
    if idade >= 60:
        lista.append({f'Indice {position}': {idade, "Idoso"}})
        print("Idoso\n")
    elif idade >= 18:
        lista.append({f'Indice {position}': {idade, "Adulto"}})
        print("Adulto\n")
    elif idade >= 13:
        lista.append({f'Indice {position}': {idade, "Adolescente"}})
        print("Adolescente\n")
    else:
        lista.append({f'Indice {position}': {idade, "Criança"}})
        print("Criança\n")


while True:
    try:
        idade = int(input("Digite uma idade - insira uma entrada diferente de number para finalizar: "))
        if idade < 0:
            print("Valor inválido, insira um valor acima de 0")
            continue
        adicionaNaLista(position, idade)
        position += 1        
    except:
        print("Dados inválidos\n")
        print("=" * 6, "Programa finalizado", "=" * 6, sep= " ")
        break


print(lista)