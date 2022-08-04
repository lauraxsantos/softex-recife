while True:
    print("1: Soma \n2: Subtração \n3: Multiplicação \n4: Divisão \n0: Sair ")
    answer = int(input(": "))
    if answer < 0 or answer > 4:
        print("Essa opção não existe")
    else:
        if answer == 0:
            break
        
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        
        if answer == 1:
            print(n1+n2)
        
        elif answer == 2:
            print(n1-n2)
            
        elif answer == 3:
            print(n1*n2)
            
        elif answer == 4: 
            print(n1/n2)
        
