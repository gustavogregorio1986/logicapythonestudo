import pandas as pd

# Dados dos alunos
dados = {
    "Nome": ["Ana", "Carlos", "Bruna", "Daniel", "Maria"],
    "Nota1": [7.5, 4.0, 8.0, 5.5, 9.0],
    "Nota2": [8.0, 5.5, 9.5, 6.0, 8.5],
    "Nota3": [9.0, 3.5, 7.5, 4.0, 10.0]
}

# Criando um DataFrame
df = pd.DataFrame(dados)

# Calculando a média das notas
df["Média"] = df[["Nota1", "Nota2", "Nota3"]].mean(axis=1)

# Definindo a nota mínima para aprovação
nota_minima = 6.0

# Determinando o status de aprovação
df["Status"] = df["Média"].apply(lambda x: "Aprovado" if x >= nota_minima else "Reprovado")

# Exibindo o DataFrame
print(df)
