from sqlalchemy import create_engine
import pandas as pd
import numpy as np


# Variáveis de conexão para o BD

host = 'localhost'
user = 'root'
password = ''
database = 'bd_loja'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Obtendo dados

df_vendas = pd.read_sql('tb_vendas', engine)

print(df_vendas)

df_vendas['valor_venda'] = df_vendas['qtd'] * df_vendas['preco']

df_vendas['comissao'] = (df_vendas['valor_venda'] * 0.09).round(2) # .round(2) para arredondar para duas casas decimais

# Converter para array

array_valor_vendas = np.array(df_vendas['valor_venda'])

media = np.mean(array_valor_vendas)
mediana = np.median(array_valor_vendas)
distancia = abs(media - mediana) / mediana

# Medidas de Tendencia Central

print(f'\n MEDIDAS DE TENDENCIA CENTRAL')
print(f'Média das comissões: R$ {media:.2f}')
print(f'Mediana das comissões: R$ {mediana:.2f}')
print(f'Distância Média e Mediana: {distancia}')
