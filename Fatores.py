# 1 - COLETA DE DADOS

# Importar a Biblioteca
import pandas as pd

# Ler o arquivo
fatores = pd.read_csv('fator_contribuinte.csv', sep=';')

# Verificar os registros e tamanhos
print('Tabela:\n',fatores.head(5).to_string())
print('\nTotal de Linha e Colunas: ', fatores.shape)

# Visão geral dos dados
print('\nTipagem da Tabela Aeronaves: \n', fatores.info())
print('\nValores nulos: \n', fatores.isnull().sum())
print('\nTotal de valores nulos: ', fatores.isnull().sum().sum() )

# Ajustar o nome da coluna
fatores.rename(columns={'codigo_ocorrencia3': 'codigo_ocorrencia'}, inplace=True)
print('Tabela tratada:\n',fatores.head(5).to_string())

# Estatística Descritiva
print('\nFrequência de fatores: \n', fatores['fator_nome'].value_counts())
print('\nFrequência de aspectos: \n', fatores['fator_aspecto'].value_counts())
print('\nFrequência de condicionantes: \n', fatores['fator_condicionante'].value_counts())
print('\nFrequência de area: \n', fatores['fator_area'].value_counts())

# LIMPEZA DOS DADOS

#Tratar dados duplicados
fatores.drop_duplicates() # remover as linhas duplicadas
print('Qtd de registros removendo as duplicadas:', len(fatores))

# Salvar Df
fatores.to_csv('fatores_tratados.csv', index=False)