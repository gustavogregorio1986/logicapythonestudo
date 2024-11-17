import pandas as pd

# Dados fictícios sobre escolas no Rio de Janeiro
dados_escolas = {
    "Escola": ["Escola A", "Escola B", "Escola C", "Escola D", "Escola E", "Escola F", "Escola G", "Escola H"],
    "Nota Média dos Alunos": [5.4, 3.8, 6.0, 4.5, 2.5, 3.0, 4.0, 6.5],  # Nota média de 0 a 10
    "Infraestrutura (1 a 10)": [7, 4, 5, 6, 3, 4, 5, 8],  # 1 é péssima, 10 é excelente
    "Taxa de Evasão (%)": [10, 25, 12, 30, 40, 35, 28, 8],  # Percentual de evasão escolar
    "Localização (1 a 10)": [6, 4, 5, 7, 3, 5, 4, 8]  # 1 é ruim, 10 é excelente
}

# Criando o DataFrame
df_escolas = pd.DataFrame(dados_escolas)

# Calculando a pontuação de risco para cada escola com base na nota média, infraestrutura e taxa de evasão
df_escolas["Pontuação de Risco"] = (
    (10 - df_escolas["Nota Média dos Alunos"]) * 0.4 +  # Quanto menor a nota, maior o risco
    (10 - df_escolas["Infraestrutura (1 a 10)"]) * 0.3 +  # Infraestrutura ruim aumenta o risco
    df_escolas["Taxa de Evasão (%)"] * 0.2 +  # Maior taxa de evasão aumenta o risco
    (10 - df_escolas["Localização (1 a 10)"]) * 0.1  # Localização ruim aumenta o risco
)

# Exibindo a tabela de escolas com as pontuações de risco
print("Tabela de Escolas com Indicadores de Desempenho:")
print(df_escolas)

# Ordenando as escolas pela pontuação de risco (maior risco no topo)
df_escolas_ordenadas = df_escolas.sort_values("Pontuação de Risco", ascending=False)

# Exibindo as escolas com maior risco (pior desempenho)
print("\nEscolas Ordenadas pela Pontuação de Risco (Pior Desempenho para Melhor Desempenho):")
print(df_escolas_ordenadas[["Escola", "Pontuação de Risco"]])
