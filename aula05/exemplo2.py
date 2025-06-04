from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import os # Necessário para uso com o dotenv

# Variáveis de conexão para o BD

# pip install python-dotenv   --  para utilizar o arquivo .env com as credenciais do BD

load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

query_vendedor = "SELECT * FROM tb_vendas WHERE nome_vendedor = 'Carlos Silva'" # Exemplo puxando apenas os dados do vendedor Carlos Silva utilizando uma query em SQL ao invés de importar todo o conteúdo da tabela.

# Obtendo dados

# df_vendas = pd.read_sql('tb_vendas', engine)

df_vendas = pd.read_sql(query_vendedor, engine)


print(df_vendas.head())

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
