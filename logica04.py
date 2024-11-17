import pandas as pd

# Simulando os dados dos candidatos
dados = {
    "Candidato": ["Lucas", "Maria", "José", "Ana", "Carlos", "Luana", "Pedro", "Fernanda", "Rafael", "Bianca"],
    "Nota": [4.5, 6.2, 3.0, 5.5, 2.8, 6.8, 4.0, 7.2, 5.9, 3.5]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Definindo a nota de corte (por exemplo, 5.0)
nota_corte = 5.0

# Adicionando uma coluna de Status (Aprovado/Reprovado)
df["Status"] = df["Nota"].apply(lambda x: "Aprovado" if x >= nota_corte else "Reprovado")

# Contando o número de aprovados e reprovados
resultado = df["Status"].value_counts()

# Verificando se a maioria dos candidatos foi reprovada
maioria_reprovados = resultado["Reprovado"] > resultado["Aprovado"]

# Exibindo os resultados
print("Resultado da prova:")
print(df)
print("\nContagem de aprovados e reprovados:")
print(resultado)

# Verificando se a maioria dos candidatos foi reprovada
if maioria_reprovados:
    print("\nA maioria dos candidatos foi reprovada.")
else:
    print("\nA maioria dos candidatos foi aprovada.")
