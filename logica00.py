import pandas as pd

dados = {
    "Nome": ["Lucila", "Laio", "Marcel", "Kaio", "Mirele", "Marcos", "Fernada", "Maria"],
    "Idade": [42, 13, 43, 23, 54, 34, 12, 21],
    "Sexo": ["Feminino", "Masculino", "Masculino", "Masculino", "Feminino", "Masculino", "Feminino", "Feminino"]
}

df = pd.DataFrame(dados)

# Corrigindo a expressão booleana com parênteses
filtro = (df["Idade"] >= 18) & (df["Sexo"] == "Masculino")

resultado = df[filtro]

print(resultado)
