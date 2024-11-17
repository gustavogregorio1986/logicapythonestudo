import pandas as pd

# Criando um DataFrame com dados fictícios
dados = {
    "Nome": ["Ana", "Carlos", "Bruna", "Daniel", "Maria"],
    "Idade": [25, 30, 22, 35, 19],
    "Salario": [2500, 3000, 2200, 4000, 1800],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Curitiba", "São Paulo", "Curitiba"]
}

df = pd.DataFrame(dados)
print(df)

# Filtrar pessoas com idade maior que 25 e salário maior que 3000
filtro = (df["Idade"] > 25) & (df["Salario"] > 3000)
resultado = df[filtro]

print("Pessoas com mais de 25 anos e salário maior que 3000:")
print(resultado)

# Adicionar uma coluna indicando se a pessoa ganha acima da média
media_salario = df["Salario"].mean()
df["Acima_da_Media"] = df["Salario"].apply(lambda x: "Sim" if x > media_salario else "Não")

print("DataFrame com nova coluna:")
print(df)

# Calcular a média salarial por cidade
media_por_cidade = df.groupby("Cidade")["Salario"].mean()

print("Média salarial por cidade:")
print(media_por_cidade)
