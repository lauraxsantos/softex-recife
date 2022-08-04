rodas = int(input("Quantidade de rodas: "))
peso = float(input("Peso em KG: "))
pessoas = int(input("Quantidade de pessoas: "))


if rodas == 3 or rodas == 2:
    print("Habilitação tipo A")
elif rodas == 4 and pessoas <= 8 and peso <= 3500:
    print("Habilitação tipo B")
elif rodas >= 4 and 3500 <= peso <= 6000:
    print("Habilitação tipo C")
elif rodas >= 4 and pessoas > 8:
    print("Habilitação tipo D")
elif rodas >= 4 and peso > 6000:
    print("Habilitação tipo E")
