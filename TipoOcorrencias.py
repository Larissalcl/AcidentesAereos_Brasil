# Importar a Biblioteca
import pandas as pd

# Ler o arquivo
tipo_ocorrencias = pd.read_csv('ocorrencia_tipo.csv', sep=';')

# Verificar os registros e tamanhos
print('Tabela:\n',tipo_ocorrencias.head(5).to_string())
print('\nTotal de Linha e Colunas: ', tipo_ocorrencias.shape)

# Visão geral dos dados
print('\nTipagem da Tabela Aeronaves: \n', tipo_ocorrencias.info())
print('\nValores nulos: \n', tipo_ocorrencias.isnull().sum())
print('\nTotal de valores nulos: ', tipo_ocorrencias.isnull().sum().sum() )

# Excluir colunas desnecessárias
tipo_ocorrencias = tipo_ocorrencias.drop(['ocorrencia_tipo_categoria','taxonomia_tipo_icao'], axis=1)

# Ajustar o nome da coluna
tipo_ocorrencias.rename(columns={'codigo_ocorrencia1': 'codigo_ocorrencia'}, inplace=True)
print('Tabela tratada:\n',tipo_ocorrencias.head(5).to_string())

#Tratar dados duplicados
tipo_ocorrencias.drop_duplicates() # remover as linhas duplicadas
print('Qtd de registros removendo as duplicadas:', len(tipo_ocorrencias))

print('\nFrequencia dos tipos : \n', tipo_ocorrencias['ocorrencia_tipo'].value_counts().head(20))

# Salvar Df
tipo_ocorrencias.to_csv('tipos_ocorrencias_tratados.csv', index=False)