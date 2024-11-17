import pandas as pd

# Dados fictícios sobre o índice de corrupção de alguns países
dados_corrupcao = {
    "País": ["Brasil", "Venezuela", "Estados Unidos", "Alemanha", "França", "Índia", "Rússia", "China"],
    "Índice de Corrupção (0 a 100)": [35, 12, 73, 80, 69, 40, 28, 42],  # 0 é muito corrupto, 100 é muito transparente
    "Ranking Global": [94, 178, 25, 10, 23, 80, 137, 80],  # Posição global no ranking de corrupção
}

# Criando o DataFrame
df_corrupcao = pd.DataFrame(dados_corrupcao)

# Exibindo a tabela com os dados
print("Tabela de Índices de Corrupção:")
print(df_corrupcao)

# Ordenando os países pelo índice de corrupção (da maior corrupção para a menor)
df_corrupcao_ordenado = df_corrupcao.sort_values("Índice de Corrupção (0 a 100)", ascending=True)

# Exibindo os países mais corruptos
print("\nPaíses com Maior Índice de Corrupção (Mais Corruptos):")
print(df_corrupcao_ordenado[["País", "Índice de Corrupção (0 a 100)"]])

# Filtrando países com índice de corrupção abaixo de 50 (mais corruptos)
df_corrupcao_mais_corruptos = df_corrupcao[df_corrupcao["Índice de Corrupção (0 a 100)"] < 50]

# Exibindo os países mais corruptos
print("\nPaíses com Índice de Corrupção Abaixo de 50 (Mais Corruptos):")
print(df_corrupcao_mais_corruptos[["País", "Índice de Corrupção (0 a 100)"]])
