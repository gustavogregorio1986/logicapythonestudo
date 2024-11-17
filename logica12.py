import pandas as pd

# Dados fictícios sobre as praias e incidentes de arrastão
dados_praias = {
    "Praia": ["Copacabana", "Ipanema", "Leblon", "Barra da Tijuca", "Arpoador", "Leme", "Flamengo", "Botafogo"],
    "Arrastões Anuais": [20, 10, 5, 30, 8, 3, 12, 15],  # Número fictício de arrastões anuais
    "Visitantes Mensais": [5000000, 4500000, 4000000, 7000000, 3500000, 3000000, 2500000, 1000000],  # Número estimado de visitantes
    "Segurança (1 a 10)": [8, 9, 10, 6, 7, 8, 7, 6],  # Nota de segurança de 1 a 10
}

# Criando o DataFrame
df_praias = pd.DataFrame(dados_praias)

# Exibindo a tabela de praias com seus dados
print("Tabela de Praias com Dados de Arrastões e Visitantes:")
print(df_praias)

# Ordenando as praias pelo número de arrastões anuais (da maior para a menor)
df_praias_ordenadas_arrastao = df_praias.sort_values("Arrastões Anuais", ascending=False)

# Exibindo as praias com mais arrastões
print("\nPraias com Mais Arrastões Anuais (Ordenadas pela Frequência de Incidentes):")
print(df_praias_ordenadas_arrastao[["Praia", "Arrastões Anuais"]])
