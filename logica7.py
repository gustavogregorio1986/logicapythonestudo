import pandas as pd

# Simulando os dados das vendas
dados = {
    "Produto": ["Celular", "Notebook", "Tablet", "Smartwatch", "Fone de Ouvido", "Teclado", "Mouse"],
    "Preço Unitário": [1200, 3000, 1500, 800, 200, 100, 50],
    "Quantidade Vendida": [50, 30, 20, 40, 100, 60, 80],
    "Categoria": ["Eletrônicos", "Eletrônicos", "Eletrônicos", "Acessórios", "Acessórios", "Acessórios", "Acessórios"]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Calculando a receita total por produto
df["Receita Total"] = df["Preço Unitário"] * df["Quantidade Vendida"]

# Calculando a receita total por categoria
receita_por_categoria = df.groupby("Categoria")["Receita Total"].sum()

# Produto mais vendido (em quantidade)
produto_mais_vendido = df[df["Quantidade Vendida"] == df["Quantidade Vendida"].max()]

# Produto que gerou mais receita
produto_maior_receita = df[df["Receita Total"] == df["Receita Total"].max()]

# Exibindo os resultados
print("DataFrame Original:")
print(df)

print("\nReceita Total por Categoria:")
