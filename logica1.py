import pandas as pd

# Criando um DataFrame a partir de um dicionário
dados = {
    "Nome": ["Ana", "Carlos", "Bruna"],
    "Idade": [25, 30, 22],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Curitiba"]
}

df = pd.DataFrame(dados)

print(df)


df = pd.read_csv("arquivo.csv")
print(df.head()) 

filtro = df[df["Idade"] > 25]  # Pessoas com mais de 25 anos
print(filtro)