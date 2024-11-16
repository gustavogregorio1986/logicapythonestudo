import pandas as pd

data = {
    "Nome":["Luiz","Pedro", "marcos", "Lenadro", "Laio","Fertnada"],
    "Idade":[23,43,23,23, 33,43],
    "Cidade":["Sao paulo","Rio de Janeiro","Sao Paulo","Sao Paulo","Curitiba","Sao Paulo"]
}

df = pd.DataFrame(data)

filtro = (df["Idade"] > 30 & (df["Cidade"] == "Sao Paulo"))
resultado = df[filtro]

print(resultado)