import pandas as pd

df = pd.read_csv("notas_alunos.csv", delimiter=",", index_col=0)
md = pd.DataFrame(columns=["media", "situacao"])

i = 0

for linha in df.itertuples():
    media = (linha[1] + linha[2])/2
    print(linha[3])
    if media >= 7 and (linha[3] == "1;" or linha[3] == "2;" or linha[3] == "3;" or linha[3] == "4;"):
        situacao = "aprovado"
    else:
        situacao = "reprovado"

    md.loc[i] = [media, situacao]
    i += 1

print(md)
