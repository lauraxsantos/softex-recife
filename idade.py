try:    
    nome = str(input("Nome completo: "))
    idade = int(input("Ano de nascimento: "))
except:
    while True:
        idade = input("Informe um ano de nascimento válido: ")
        if idade.isdigit():
            break

print(2022-int(idade))
