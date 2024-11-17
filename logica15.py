import pandas as pd

# Dados fictícios sobre vendas de produtos
dados_vendas = {
    "Produto": ["Notebook", "Smartphone", "Tablet", "Fone de Ouvido", "Monitor", "Teclado"],
    "Jan": [120, 300, 200, 150, 180, 220],
    "Fev": [110, 310, 210, 160, 190, 230],
    "Mar": [130, 290, 190, 170, 200, 240],
    "Abr": [140, 280, 220, 180, 210, 250],
    "Mai": [150, 330, 230, 190, 220, 260],
}

# Criando o DataFrame
df_vendas = pd.DataFrame(dados_vendas)

# Exibindo a tabela com as vendas mensais
print("Tabela de Vendas de Produtos:")
print(df_vendas)

# Calculando o total de vendas de cada produto
df_vendas['Total de Vendas'] = df_vendas.iloc[:, 1:].sum(axis=1)

# Calculando a média de vendas por produto
df_vendas['Média de Vendas'] = df_vendas.iloc[:, 1:-1].mean(axis=1)

# Ordenando os produtos pelo total de vendas (do maior para o menor)
df_vendas_ordenado = df_vendas.sort_values('Total de Vendas', ascending=False)

# Exibindo o ranking de produtos mais vendidos
print("\nRanking de Produtos Mais Vendidos:")
print(df_vendas_ordenado[["Produto", "Total de Vendas"]])

# Exibindo a média de vendas de cada produto
print("\nMédia de Vendas Mensais por Produto:")
print(df_vendas[["Produto", "Média de Vendas"]])

# Exibindo o produto com maior média de vendas
produto_top_venda = df_vendas.loc[df_vendas['Média de Vendas'].idxmax()]
print("\nProduto com Maior Média de Vendas:")
print(produto_top_venda[["Produto", "Média de Vendas"]])
