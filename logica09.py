import pandas as pd

# Dados fictícios sobre os bairros do RJ
dados_bairros = {
    "Bairro": ["Centro", "Cachambi", "Cidade de Deus", "Vila Kennedy", "Jacarezinho", "Complexo do Alemão", "Bangu", "Madureira"],
    "Preço Médio Aluguel (R$)": [1500, 1000, 800, 900, 600, 500, 1200, 700],
    "Taxa de Criminalidade (1 a 10)": [9, 8, 10, 9, 10, 10, 7, 6],  # Quanto maior, mais violento
    "Segurança (1 a 10)": [3, 4, 2, 3, 2, 2, 5, 6],  # Quanto menor, menos seguro
    "Acessibilidade (1 a 10)": [6, 7, 5, 6, 4, 4, 6, 7],  # Facilidade de deslocamento
}

# Criando o DataFrame
df_bairros = pd.DataFrame(dados_bairros)

# Calculando a pontuação de risco para cada bairro, levando em conta a criminalidade e a segurança
df_bairros["Pontuação de Risco"] = (
    df_bairros["Taxa de Criminalidade (1 a 10)"] * 0.5 +  # A criminalidade tem maior peso
    (10 - df_bairros["Segurança (1 a 10)"]) * 0.4 +  # Menor segurança aumenta o risco
    (10 - df_bairros["Preço Médio Aluguel (R$)"] / 1000) * 0.1  # Preço menor pode indicar maior violência em alguns casos
)

# Exibindo os dados
print("Tabela de Bairros com Indicadores de Violência:")
print(df_bairros)

# Ordenando os bairros pela pontuação de risco (maior risco no topo)
df_bairros_ordenado = df_bairros.sort_values("Pontuação de Risco", ascending=False)

# Exibindo os bairros mais violentos
print("\nBairros Ordenados pela Pontuação de Risco (Mais Violentos para Menos Violentos):")
print(df_bairros_ordenado[["Bairro", "Pontuação de Risco"]])
