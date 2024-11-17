import pandas as pd

# Criando o dicionário de produtos
dicionario_produtos = {
    "nome": ["iphone", "ipad", "airpod"],
    "preco": [5000, 9000, 2000],
    "estoque": [100, 50, 60]
}

# Criando o DataFrame com os dados
df = pd.DataFrame(dicionario_produtos)

# Exibindo o DataFrame
print(df)
