import pandas as pd

# Dados fictícios sobre os bairros do RJ
dados_bairros = {
    "Bairro": ["Botafogo", "Ipanema", "Leblon", "Barra da Tijuca", "Tijuca", "Santa Teresa", "Méier"],
    "Preço Médio Aluguel (R$)": [3000, 5000, 7000, 2500, 1500, 2000, 1200],
    "Segurança (1 a 10)": [8, 9, 10, 7, 6, 7, 5],
    "Proximidade a Áreas Verdes (1 a 10)": [9, 9, 10, 8, 10, 7, 6],
    "Acessibilidade (1 a 10)": [8, 9, 9, 7, 8, 7, 6]
}

# Criando o DataFrame
df_bairros = pd.DataFrame(dados_bairros)

# Calculando uma pontuação para cada bairro com base nos critérios
df_bairros["Pontuação Geral"] = (
    df_bairros["Segurança (1 a 10)"] * 0.3 +
    df_bairros["Proximidade a Áreas Verdes (1 a 10)"] * 0.3 +
    df_bairros["Acessibilidade (1 a 10)"] * 0.2 +
    (10 - df_bairros["Preço Médio Aluguel (R$)"] / 1000) * 0.2  # Valorizando bairros mais baratos
)

# Exibindo os dados
print("Tabela de Bairros do RJ com Critérios de Avaliação:")
print(df_bairros)

# Ordenando os bairros pela pontuação geral
df_bairros_ordenado = df_bairros.sort_values("Pontuação Geral", ascending=False)

# Exibindo os bairros ordenados
print("\nBairros Ordenados pela Pontuação Geral (Melhor para Pior):")
print(df_bairros_ordenado[["Bairro", "Pontuação Geral"]])
