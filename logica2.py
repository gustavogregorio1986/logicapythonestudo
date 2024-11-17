import pandas as pd

# Configurando os números para a tabuada (exemplo: 1 a 10)
numeros = list(range(1, 11))  # Números de 1 a 10
resultados = {}

# Construindo as tabuadas
for numero in numeros:
    resultados[f"Tabuada de {numero}"] = [numero * i for i in range(1, 11)]

# Criando um DataFrame com os resultados
df = pd.DataFrame(resultados, index=[f"{i} x" for i in range(1, 11)])

# Exibindo a tabela de tabuadas
print(df)
