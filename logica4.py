import pandas as pd

# Função para criar o DataFrame inicial
def criar_dataframe():
    numeros = {
        "Número 1": [10, 20, 30, 40, 50],
        "Número 2": [5, 15, 25, 35, 45]
    }
    return pd.DataFrame(numeros)

# Função da calculadora
def calculadora(df):
    # Adicionando operações ao DataFrame
    df["Soma"] = df["Número 1"] + df["Número 2"]
    df["Subtração"] = df["Número 1"] - df["Número 2"]
    df["Multiplicação"] = df["Número 1"] * df["Número 2"]
    df["Divisão"] = df["Número 1"] / df["Número 2"]
    df["Potência"] = df["Número 1"] ** 2
    df["Raiz Quadrada"] = df["Número 1"].apply(lambda x: x ** 0.5)
    return df

# Criar DataFrame inicial
df = criar_dataframe()

# Aplicar a calculadora
resultado = calculadora(df)

# Exibir os resultados
print("Tabela de Operações:")
print(resultado)
