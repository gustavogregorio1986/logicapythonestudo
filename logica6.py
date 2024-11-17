import pandas as pd

# Simulando os dados dos funcionários
dados = {
    "Nome": ["João", "Maria", "Pedro", "Ana", "Carlos", "Fernanda", "Luiz", "Clara"],
    "Idade": [35, 29, 40, 25, 50, 30, 45, 27],
    "Cargo": ["Analista", "Gerente", "Analista", "Estagiário", "Diretor", "Analista", "Gerente", "Estagiário"],
    "Salario": [5000, 8000, 5200, 1500, 15000, 5100, 8500, 1400]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Agrupando os funcionários por cargo e calculando o salário médio
salario_medio_por_cargo = df.groupby("Cargo")["Salario"].mean()

# Encontrando o funcionário com maior e menor salário
maior_salario = df[df["Salario"] == df["Salario"].max()]
menor_salario = df[df["Salario"] == df["Salario"].min()]

# Contando a quantidade de funcionários por cargo
funcionarios_por_cargo = df["Cargo"].value_counts()

# Exibindo os resultados
print("DataFrame Original:")
print(df)

print("\nSalário Médio por Cargo:")
print(salario_medio_por_cargo)

print("\nFuncionário com Maior Salário:")
print(maior_salario)

print("\nFuncionário com Menor Salário:")
print(menor_salario)

print("\nQuantidade de Funcionários por Cargo:")
print(funcionarios_por_cargo)
