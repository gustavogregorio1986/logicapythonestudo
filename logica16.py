import pandas as pd

# Dados fictícios de roubos de celulares no RJ
dados_roubos = {
    "Ano": [2019, 2020, 2021, 2022, 2023, 2024],
    "Roubos de Celulares": [12000, 13000, 14000, 15000, 16000, 17000]  # número de celulares roubados por ano
}

# Criando o DataFrame
df_roubos = pd.DataFrame(dados_roubos)

# Exibindo o DataFrame
print("Dados de Roubos de Celulares no RJ (2019-2024):")
print(df_roubos)

# Total de roubos entre 2019 e 2022
total_2019_2022 = df_roubos[df_roubos["Ano"] <= 2022]["Roubos de Celulares"].sum()

# Total de roubos entre 2023 e 2024
total_2023_2024 = df_roubos[df_roubos["Ano"] >= 2023]["Roubos de Celulares"].sum()

# Exibindo os totais para cada período
print("\nTotal de roubos de celulares entre 2019-2022:", total_2019_2022)
print("Total de roubos de celulares entre 2023-2024:", total_2023_2024)

# Comparando os dois períodos
porcentagem_aumento = ((total_2023_2024 - total_2019_2022) / total_2019_2022) * 100
print(f"\nAumento percentual de roubos de celulares entre 2023-2024 em relação a 2019-2022: {porcentagem_aumento:.2f}%")
