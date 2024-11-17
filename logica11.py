import pandas as pd

# Dados fictícios sobre praias
dados_praias = {
    "Praia": ["Copacabana", "Ipanema", "Leblon", "Barra da Tijuca", "Arpoador", "Leme", "Flamengo", "Botafogo"],
    "Visitantes Mensais": [5000000, 4500000, 4000000, 7000000, 3500000, 3000000, 2500000, 1000000],  # Número estimado de visitantes mensais
    "Localização": ["Zona Sul", "Zona Sul", "Zona Sul", "Zona Oeste", "Zona Sul", "Zona Sul", "Zona Sul", "Zona Sul"],
    "Segurança (1 a 10)": [8, 9, 10, 6, 7, 8, 7, 6],  # Nota de segurança de 1 a 10
}

# Criando o DataFrame
df_praias = pd.DataFrame(dados_praias)

# Exibindo a tabela de praias com seus dados
print("Tabela de Praias com Dados de Visitantes e Localização:")
print(df_praias)

# Ordenando as praias por número de visitantes mensais (da mais frequentada para a menos frequentada)
df_praias_ordenadas = df_praias.sort_values("Visitantes Mensais", ascending=False)

# Exibindo as praias mais frequentadas
print("\nPraias Mais Frequentadas (Ordenadas por Visitantes Mensais):")
print(df_praias_ordenadas[["Praia", "Visitantes Mensais"]])
