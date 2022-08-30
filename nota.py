maiornotaA = 0
aprovadoA = 0
maiorB = 0
aprovadoB = 0

maiorC = 0
aprovadoC = 0

alunoA = ""
alunoB = ""
alunoC = ""
alunoNota = " "

maiorD = 0
aprovadoD = 0


for i in range(100):
    nome = str(input("Nome: ")).capitalize()
    nota = float(input("Nota: "))
    turma = str(input("Turma: ")).upper()

    if turma == "A":
        if nota >= 7:
            aprovadoA += 1
        if nota >= maiornotaA:
            maiornotaA = nota
            alunoA = nome

    if turma == "B":
        if nota >= 7:
            aprovadoB += 1
        if nota >= maiorB:
            maiorNotaTurmaB = nota
            alunoB = nome

    if turma == "C":
        if nota >= 7:
            aprovadoC += 1
        if nota >= maiorC:
            maiorC = nota
            alunoC = nome

    if turma == "D":
        if nota >= 7:
            aprovadoD += 1
        if nota >= maiorD:
            maiorD = nota
            alunoD = nome

if maiornotaA > maiorB and maiornotaA > maiorC and maiornotaA > maiorD:
    alunoNota = alunoA

elif maiorB > maiornotaA and maiorB > maiorC and maiorB > maiorD:
    alunoNota = alunoB

elif maiorC > maiornotaA and maiorC > maiorB and maiorC > maiorD:
    alunoNota = alunoC

else:
    alunoNota = alunoD

print("Aprovados por turma:")
print(f"Turma A:{aprovadoA}, Turma B:{aprovadoB}, Turma C:{aprovadoC}, Turma D:{aprovadoD}")
print("----------------")

print("Maior nota por Turma:")
print(f"Turma A: {maiornotaA}, Turma B:{maiorB}, Turma C: {maiorC}, Turma D{maiorD}")
print("--------------------")

print(f"Aluno com maior nota: {alunoNota}")
