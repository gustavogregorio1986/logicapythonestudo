import pandas as pd

# Criando um DataFrame com números
dados = {
    "Numeros": [10, 15, 20, 25, 30, 35, 40],
    "Categoria": ["A", "B", "A", "C", "A", "B", "C"]
}

df = pd.DataFrame(dados)

# Filtrar apenas números maiores que 20
filtro = df["Numeros"] > 20
resultado = df[filtro]

print("Filtrando números maiores que 20:")
print(resultado)


# Adicionando uma nova coluna com o dobro dos números
df["Dobro"] = df["Numeros"] * 2
print("Com a nova coluna Dobro:")
print(df)

# Filtrar apenas os números pares
pares = df[df["Numeros"] % 2 == 0]
print("Números pares:")
print(pares)

# Elevar os números ao quadrado
df["Quadrado"] = df["Numeros"].apply(lambda x: x ** 2)
print("Com a coluna Quadrado:")
print(df)

# Adicionar uma coluna indicando se o número é par ou ímpar
df["Par_ou_Impar"] = df["Numeros"].apply(lambda x: "Par" if x % 2 == 0 else "Ímpar")

# Filtrar números da categoria A com valores acima de 15
resultado = df[(df["Categoria"] == "A") & (df["Numeros"] > 15)]

print("Resultado final:")
print(df)
print("Filtrados da categoria A com números > 15:")
print(resultado)
