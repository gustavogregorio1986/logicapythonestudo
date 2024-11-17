import pandas as pd

# Dados das notas dos alunos
dados = {
    "Aluno": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel"],
    "Matemática": [8.5, 4.0, 6.0, 7.5, 3.0, 9.0, 5.5],
    "Português": [7.0, 5.0, 8.0, 6.5, 2.5, 7.5, 4.0],
    "Ciências": [9.0, 3.5, 5.5, 8.0, 4.0, 6.0, 6.5],
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Média geral de cada aluno
df["Média Geral"] = df[["Matemática", "Português", "Ciências"]].mean(axis=1)


# Situação do aluno com base na média
def situacao(media):
    if media >= 7.0:
        return "Aprovado"
    elif 5.0 <= media < 7.0:
        return "Recuperação"
    else:
        return "Reprovado"

df["Situação"] = df["Média Geral"].apply(situacao)

# Exibindo os resultados
print("Notas dos Alunos:")
print(df)

# Estatísticas gerais
aprovados = df[df["Situação"] == "Aprovado"]
reprovados = df[df["Situação"] == "Reprovado"]
recuperacao = df[df["Situação"] == "Recuperação"]

print(f"\nTotal de Aprovados: {len(aprovados)}")
print(f"Total de Reprovados: {len(reprovados)}")
print(f"Total em Recuperação: {len(recuperacao)}")
