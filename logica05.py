import pandas as pd

# Simulando os dados das vendas
dados = {
    "Produto": ["Camiseta", "Calça", "Tênis", "Camiseta", "Calça", "Tênis", "Camiseta", "Boné"],
    "Quantidade": [10, 5, 2, 8, 3, 6, 1, 4],
    "Preço": [50, 100, 300, 50, 100, 300, 50, 25],
    "Data": ["2024-11-01", "2024-11-02", "2024-11-02", "2024-11-03", "2024-11-03", "2024-11-04", "2024-11-04", "2024-11-05"]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Calculando a Receita (Quantidade * Preço)
df["Receita"] = df["Quantidade"] * df["Preço"]

# Total de vendas por produto
vendas_por_produto = df.groupby("Produto")["Quantidade"].sum()

# Receita total
receita_total = df["Receita"].sum()

# Produto mais vendido
produto_mais_vendido = vendas_por_produto.idxmax()

# Exibindo os dados
print("DataFrame Original:")
print(df)

print("\nVendas por Produto:")
print(vendas_por_produto)

print(f"\nReceita Total: R$ {receita_total:.2f}")

print(f"\nProduto Mais Vendido: {produto_mais_vendido}")
