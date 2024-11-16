import pandas as pd

data = {
    "Nome":["Marcos","Luiz","Michel","Maycon", "Mirele","Michele"],
    "Idade":[34,23,43,23,11,12]
}

df = pd.DataFrame(data)

filtro  = (df["Idade"] > 18)

resultado = df[filtro]

print(resultado)