print("Escolha um dos meios de transporte abaixo!")
print("-Trator\n"
      "-Moto.\n"
      "-Bicicleta \n"
      "-Trem\n"
      "- Carro\n"
      "- Caminhão \n"
      "- Ônibus\n"
      "- Paraquedas\n"
      "- Balão \n"
      "- Avião \n"
      "- Helicóptero \n"
      "- Submarino \n"
      "- Barco \n"
      "- Navio \n"
      "- Lancha\n"
      )
terrestre = str(input("É terrestre?")).lower()
if terrestre == "sim":
    t1 = str(input("Cabe apenas uma pessoa?")).lower()
    if t1 == "sim":
        t2 = str(input("É pesado?")).lower()
        if t2 == "sim":
            print("Então, o transporte escolhido foi um trator")
        else:
            t3 = str(input("Tem pedal?")).lower()
            if t3 == "sim":
                print("Então, o transporte escolhido foi uma bicleta")
    else:
        capacete = str(input("Usa capacete?")).lower()
        if capacete == "sim":
            print("Então, o transporte escolhido foi uma moto")
        if capacete == "nao":
            trilho = str(input("Usa trilho?"))
            if trilho == "Sim":
                print("Então, o transporte escolhido foi um trem")
            else:
                alto = str(input("O transporte é alto?")).lower()
                if alto == "sim":
                    carroceria = str(input("Usa carroceria?"))
                    if carroceria == "Sim":
                        print("Então o seu transporte é um caminhão")
                    else:
                        print("Então, o seu transporte é um ônibus")
                else:
                    print("Então, o seu transporte é um carro")
if terrestre == "nao":
    voa = str(input("É aéreo?")).lower()
    if voa == "sim":
        pular = input("Precisa pular?").lower()
        if pular == "sim":
            print("Então seu transporte é uma asa delta")
        else:
            devagar = input("É devagar?").lower()
            if devagar == "sim":
                print("Então seu transporte é um balão")
            else:
                asa = input("Ele possui asas fixas?").lower()
                if asa == "sim":
                    print("Então, seu transporte é o avião")
                else:
                    print("Então, seu transporte é um helicóptero")
    if voa == "nao":
        aquat = input("É aquático?").lower()
        if aquat == "sim":
            agua = input("Seu transporte fica coberto por água?").lower()
            if agua == "sim":
                print("Então, o seu transporte é um submarino")
            else:
                vela = input("Possui vela?").lower()
                if vela == "sim":
                    print("Então, o seu veiculo é um barco")
                else:
                    motor = input("Seu veiculo tem motor?").lower()
                    if motor == "sim":
                        alto = input("Seu veiculo é alto?").lower()
                        if alto == "sim":
                            print("Então, o seu transporte é um navio")
                        if alto == "nao":
                            descoberto = input("O seu veiculo pode ser descoberto?").lower()
                            if descoberto == "sim":
                                print("Então, o seu veiculo é uma lancha")
