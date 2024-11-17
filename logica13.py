import pandas as pd

# Dados fictícios sobre restaurantes
dados_restaurantes = {
    "Restaurante": ["Sushi Samba", "Churrascaria Fogo de Chão", "La Trattoria", "Oro", "Cipriani", "Gigoia Sushi", "Zuka", "Mamma Jamma"],
    "Categoria": ["Sushi", "Churrasco", "Italiana", "Gastronomia Brasileira", "Gastronomia Internacional", "Sushi", "Gastronomia Internacional", "Italiana"],
    "Preço Médio (R$)": [100, 150, 80, 200, 250, 90, 180, 70],  # Preço médio por pessoa
    "Avaliação (1 a 5)": [4.5, 4.8, 4.0, 4.9, 5.0, 4.3, 4.7, 4.2],  # Avaliação média dos clientes
    "Localização": ["Ipanema", "Barra da Tijuca", "Leblon", "Botafogo", "Copacabana", "Lagoa", "Leblon", "Ipanema"]
}

# Criando o DataFrame
df_restaurantes = pd.DataFrame(dados_restaurantes)

# Exibindo a tabela de restaurantes com seus dados
print("Tabela de Restaurantes:")
print(df_restaurantes)

# Ordenando os restaurantes por avaliação (da maior para a menor)
df_restaurantes_ordenados_avaliacao = df_restaurantes.sort_values("Avaliação (1 a 5)", ascending=False)

# Exibindo os restaurantes mais bem avaliados
print("\nRestaurantes Mais Bem Avaliados (Ordenados pela Avaliação):")
print(df_restaurantes_ordenados_avaliacao[["Restaurante", "Avaliação (1 a 5)"]])

# Filtrando restaurantes que possuem preço médio acima de 150
df_restaurantes_caros = df_restaurantes[df_restaurantes["Preço Médio (R$)"] > 150]

# Exibindo os restaurantes caros
print("\nRestaurantes com Preço Médio Acima de R$150:")
print(df_restaurantes_caros[["Restaurante", "Preço Médio (R$)"]])
