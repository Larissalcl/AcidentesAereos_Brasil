# 1 - COLETA DE DADOS

# Importar a Biblioteca
import pandas as pd
import  numpy as np

# Ler o arquivo
recomendacao = pd.read_csv('recomendacao.csv', sep=';')

# Verificar os registros e tamanhos
print('Tabela:\n',recomendacao.head(5).to_string())
print('\nTotal de Linha e Colunas: ', recomendacao.shape)

# Visão geral dos dados
print('\nTipagem da Tabela Aeronaves: \n', recomendacao.info())
print('\nValores nulos: \n', recomendacao.isnull().sum())
print('\nTotal de valores nulos: ', recomendacao.isnull().sum().sum())

# Ajustar o nome da coluna
recomendacao.rename(columns={'codigo_ocorrencia4': 'codigo_ocorrencia'}, inplace=True)
print('Tabela tratada:\n',recomendacao.head(5).to_string())

#Tratar dados duplicados
recomendacao.drop_duplicates() # remover as linhas duplicadas
print('Qtd de registros removendo as duplicadas:', len(recomendacao))

#Tratar valores nulos
recomendacao.fillna({'recomendacao_dia_feedback': 'Não Informado'}, inplace=True)

print('\nTotal de valores nulos: ', recomendacao.isnull().sum().sum())

# Salvar Df
recomendacao.to_csv('recomendacao_tratados.csv', index=False)