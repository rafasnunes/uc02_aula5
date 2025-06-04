from sqlalchemy import create_engine
import pandas as pd
import numpy as np


# Variáveis de conexão para o BD

host = 'localhost'
user = 'root'
password = ''
database = 'bd_loja'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Obtendo os dados

df_estoque = pd.read_sql('tb_produtos', engine)

print(df_estoque.head()) # .head limita a quantidade de linhas as 5 primeiras

df_estoque['TotalEstoque'] = df_estoque['qtd'] * df_estoque['preco']
print(df_estoque[['produto', 'TotalEstoque']])
print(f'\nTotal Geral de Produtos: R$ {df_estoque["TotalEstoque"].sum()}')

# Numpy

array_estoque = np.array(df_estoque['TotalEstoque']) # Transformei a coluna TotalEstoque da série para array para poder manipular com calculos matematicos de forma mais eficaz com numpy.

# print(array_estoque)

media = np.mean(array_estoque)
mediana = np.median(array_estoque)
distancia = abs(media - mediana) / mediana


print(f'Media = {media:.2f}')
print(f'Mediana = {mediana:.2f}')
print(f'Distância Média e Mediana: {distancia}')