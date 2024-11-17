import pandas as pd

# Dados fictícios
dados = {
    "Rua": ["Rua A", "Rua B", "Rua C", "Rua D", "Rua E", "Rua F", "Rua G"],
    "Bairro": ["Nova Iguaçu", "Duque de Caxias", "Nilópolis", "Mesquita", "São João de Meriti", "Queimados", "Belford Roxo"],
    "Acesso a Luz": ["Sim", "Não", "Sim", "Sim", "Não", "Sim", "Não"]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Total de endereços
total_enderecos = len(df)

# Total de endereços com luz
enderecos_com_luz = len(df[df["Acesso a Luz"] == "Sim"])

# Total de endereços sem luz
enderecos_sem_luz = len(df[df["Acesso a Luz"] == "Não"])

# Exibindo os dados
print("Tabela de Endereços:")
print(df)

print(f"\nTotal de Endereços: {total_enderecos}")
print(f"Total com Acesso à Luz: {enderecos_com_luz}")
print(f"Total sem Acesso à Luz: {enderecos_sem_luz}")
