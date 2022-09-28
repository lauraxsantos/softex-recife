
nome = str(input("Digite seu nome: "))
lista = str(input("Digite um conjunto de caracteres: "))
titulo = str(input("Título: "))


def maiusculo(nome):
    return nome.upper()


def replace(lista):
    return lista.replace("a", "@")


def tit(titulo):
    return titulo.capitalize()


print(maiusculo(nome))
print(replace(lista))
print(tit(titulo))
