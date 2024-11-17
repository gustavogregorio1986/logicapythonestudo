import pandas as pd

# Simulando os dados dos alunos
dados = {
    "Aluno": ["Ana", "João", "Maria", "Pedro", "Clara", "Luiz", "Fernanda", "Carlos"],
    "Nota1": [8.0, 5.5, 7.0, 4.0, 9.5, 6.0, 5.0, 3.5],
    "Nota2": [7.5, 6.0, 8.0, 5.0, 8.0, 6.5, 4.5, 2.0]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Adicionando uma coluna para a média das notas
df["Media"] = (df["Nota1"] + df["Nota2"]) / 2

# Definindo o status de aprovação
df["Status"] = df["Media"].apply(lambda x: "Aprovado" if x >= 6 else "Reprovado")

# Separando os alunos aprovados e reprovados
aprovados = df[df["Status"] == "Aprovado"]
reprovados = df[df["Status"] == "Reprovado"]

# Exibindo os dados
print("DataFrame Original:")
print(df)

print("\nAlunos Aprovados:")
print(aprovados)

print("\nAlunos Reprovados:")
print(reprovados)

# Estatísticas adicionais
print(f"\nNúmero de Aprovados: {len(aprovados)}")
print(f"Número de Reprovados: {len(reprovados)}")
print(f"Média Geral da Turma: {df['Media'].mean():.2f}")
