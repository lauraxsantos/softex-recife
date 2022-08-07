from enum import Enum
x = y = z = nulo = bra = voto = 0



class Voto(Enum):
    candidato_X = 889
    candidato_Y = 847
    candidato_Z = 515
    branco = 0


while True:
    try:
        v = int(input("Digite seu voto: "))
        if v == Voto.candidato_X.value:
            x += 1
        elif v == Voto.candidato_Y.value:
            y += 1
        elif v == Voto.candidato_Z.value:
            z += 1
        elif v == Voto.branco.value:
            bra += 1
        elif v != Voto.candidato_Z.value and v != Voto.candidato_X.value and v != Voto.candidato_Y.value and v != Voto.branco:
            nulo += 1

        resp = str(input("Deseja finalizar a votação? ")).lower()
        if resp == "sim":
            break
    except:
       print("Insira um voto válido")

print(f"Candidato X = {x}")
print(f"Candidato Y = {y}")
print(f"Candidato Z = {z}")
print(f"Brancos = {bra} e Nulos = {nulo}")
