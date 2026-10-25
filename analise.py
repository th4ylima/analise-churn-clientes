import pandas as pd

# 1. Dados simulados integrados direto no código (Independente de Banco de Dados externo)
dados_ficticios = {
    'id_cliente': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015],
    'idade': [28, 34, 41, 29, 46, 31, 36, 52, 38, 27, 42, 33, 30, 45, 40],
    'tipo_contrato': ['Mensal','Anual','Mensal','Mensal','Anual','Mensal','Trimestral','Mensal','Trimestral','Anual','Mensal','Mensal','Mensal','Anual','Trimestral'],
    'mensalidade': [89.9, 59.9, 89.9, 79.9, 49.9, 89.9, 69.9, 79.9, 69.9, 49.9, 89.9, 79.9, 89.9, 59.9, 69.9],
    'meses_contrato': [1, 12, 1, 1, 12, 1, 3, 1, 3, 12, 1, 1, 1, 12, 3],
    'cancelou': [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0]
}

# 2. Criando o DataFrame do Pandas
df = pd.DataFrame(dados_ficticios)
print("DataFrame criado com sucesso!\n")

# --- Estatística Descritiva Aplicada ---

# Insight 1: Métrica Geral de Negócio (Taxa de Churn)
taxa_churn = df['cancelou'].mean() * 100
print(f"Taxa Geral de Churn: {taxa_churn:.2f}%")

# Insight 2: Média de Idade (Quem cancela costuma ser mais jovem?)
print("\nMédia de idade (Clientes Ativos [0] vs Cancelados [1]):")
print(df.groupby('cancelou')['idade'].mean())

# Insight 3: Tipo de contrato impacta no cancelamento?
print("\nQuantidade de cancelamentos por Tipo de Contrato:")
print(pd.crosstab(df['tipo_contrato'], df['cancelou']))

# 3. Exportando a base limpa para gerar os gráficos no Power BI
df.to_csv('dados_clientes_limpos.csv', index=False)
print("\nSucesso! O arquivo 'dados_clientes_limpos.csv' foi gerado na sua pasta.")
