import pandas as pd

# Dados do estoque
dados = {
    "Produto": ["Arroz", "Feijão", "Macarrão", "Óleo", "Açúcar", "Farinha", "Leite"],
    "Estoque Atual": [50, 20, 15, 10, 30, 5, 12],
    "Estoque Mínimo": [30, 25, 20, 15, 35, 10, 10],
    "Preço Unitário (R$)": [5.0, 7.0, 3.5, 6.0, 4.0, 8.0, 4.5]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Identificando os produtos com estoque abaixo do mínimo
df["Reposição Necessária"] = df["Estoque Mínimo"] - df["Estoque Atual"]
df["Reposição Necessária"] = df["Reposição Necessária"].apply(lambda x: x if x > 0 else 0)

# Calculando o custo para reposição de cada produto
df["Custo Reposição (R$)"] = df["Reposição Necessária"] * df["Preço Unitário (R$)"]

# Produtos que precisam de reposição
produtos_para_repor = df[df["Reposição Necessária"] > 0]

# Exibindo os resultados
print("Controle de Estoque:")
print(df)

print("\nProdutos que precisam de reposição:")
print(produtos_para_repor)

print(f"\nCusto total de reposição: R$ {produtos_para_repor['Custo Reposição (R$)'].sum():,.2f}")
