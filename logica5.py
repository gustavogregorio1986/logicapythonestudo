import pandas as pd
from datetime import datetime

# Simulando os dados dos alunos
dados = {
    "Aluno": ["Lucas", "Maria", "José", "Ana", "Carlos", "Luana", "Pedro", "Fernanda", "Rafael", "Bianca"],
    "Data_Entrada": ["2023-12-20", "2023-11-15", "2023-12-22", "2023-12-18", "2023-12-23", 
                     "2023-11-30", "2023-12-15", "2023-12-25", "2023-12-01", "2023-12-10"],
    "Data_Saida": ["2024-01-10", "2023-12-05", "2024-01-05", "2023-12-20", "2024-01-05", 
                   "2023-12-25", "2024-01-15", "2024-01-07", "2024-01-12", "2023-12-30"]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Convertendo as datas para o formato datetime
df["Data_Entrada"] = pd.to_datetime(df["Data_Entrada"])
df["Data_Saida"] = pd.to_datetime(df["Data_Saida"])

# Definindo o período de férias (final de ano)
data_inicio_ferias = datetime(2023, 12, 15)
data_fim_ferias = datetime(2024, 1, 10)

# Determinando se o aluno está de férias
df["De_Ferias"] = (df["Data_Entrada"] >= data_inicio_ferias) & (df["Data_Saida"] <= data_fim_ferias)

# Exibindo os resultados
print("Status dos alunos de férias:")
print(df[["Aluno", "Data_Entrada", "Data_Saida", "De_Ferias"]])
