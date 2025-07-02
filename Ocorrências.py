# 1 - COLETA DE DADOS

# Importar a Biblioteca
import pandas as pd
from datetime import datetime, time
import  numpy as np

# Ler o arquivo
ocorrencias = pd.read_csv('ocorrencia.csv', sep=';')

# Verificar os registros e tamanhos
print('Tabela:\n',ocorrencias.head(5).to_string())
print('\nTotal de Linha e Colunas: ', ocorrencias.shape)

# Visão geral dos dados
print('\nTipagem da Tabela Aeronaves: \n', ocorrencias.info())
print('\nValores nulos: \n', ocorrencias.isnull().sum())
print('\nTotal de valores nulos: ', ocorrencias.isnull().sum().sum() )

# Excluir colunas desnecessárias
ocorrencias = ocorrencias.drop(['codigo_ocorrencia1', 'codigo_ocorrencia2', 'codigo_ocorrencia3', 'codigo_ocorrencia4', 'ocorrencia_latitude', 'ocorrencia_longitude', 'divulgacao_relatorio_numero', 'divulgacao_dia_publicacao'], axis=1)

print('Tabela Tratada:\n',ocorrencias.head(5).to_string())
print('\nValores nulos: \n', ocorrencias.isnull().sum())
print('\nTotal de valores nulos: ', ocorrencias.isnull().sum().sum() )

# Estatística Descritiva
print('\nEstatistica do df: \n', ocorrencias.describe())
print('\nFrequência de Classificação: \n', ocorrencias['ocorrencia_classificacao'].value_counts())
print('\nFrequência de Estado: \n', ocorrencias['ocorrencia_uf'].value_counts())
print('\nFrequência de Status da Investigação: \n', ocorrencias['investigacao_status'].value_counts())
print('\nFrequência de Saída de Pista: \n', ocorrencias['ocorrencia_saida_pista'].value_counts())

# 3 - LIMPEZA DOS DADOS

#Tratar valores duplicados
ocorrencias.drop_duplicates()
print('Qtd de registros removendo as duplicadas:', len(ocorrencias))

#Excluir Linhas com mais 7 registros nulos
ocorrencias = ocorrencias.dropna(thresh=7)
print('Qtd total de registros nulos após exclusão:', ocorrencias.isnull().sum().sum())

#Preencher valor nulos com não informado
ocorrencias.fillna({'investigacao_aeronave_liberada': 'Não Informado',
                   'investigacao_status': 'Não Informado',},
                  inplace=True)

#Preencher valor nulos com a média
media = pd.to_timedelta(ocorrencias['ocorrencia_hora'].dropna().astype(str)).mean()
ocorrencias['ocorrencia_hora'] = ocorrencias['ocorrencia_hora'].fillna((pd.Timestamp('1900-01-01') + media).time())

print('\nTotal de valores nulos após tratamento: ', ocorrencias.isnull().sum().sum() )

print('\nTipagem da Tabela: \n', ocorrencias.info())

# Converter tipo de dado para data/hora
ocorrencias['ocorrencia_dia'] =  pd.to_datetime(ocorrencias['ocorrencia_dia'],format='%d/%m/%Y', errors='coerce')
ocorrencias['ocorrencia_hora'] = pd.to_datetime(ocorrencias['ocorrencia_hora'], format='%H:%M:%S', errors='coerce')

# Extrair apenas a hora
ocorrencias['ocorrencia_hora'] = ocorrencias['ocorrencia_hora'].dt.time

print('\nTipagem após tratamento: \n', ocorrencias.info())

# Criar coluna de ano
ocorrencias['ocorrencia_ano'] = ocorrencias['ocorrencia_dia'].dt.year

#Ajustar a posição da coluna 'ano'
colunas = ocorrencias.columns.tolist()
colunas.insert(7, colunas.pop(colunas.index('ocorrencia_ano')))
ocorrencias = ocorrencias[colunas]

#Transformar a variável horário em categorias
def categoriza_turno(h):
    if pd.isna(h):  # Trata valores nulos
        return 'Desconhecido'
    if time(6, 0) <= h < time(12, 0):
        return 'Manhã'
    elif time(12, 0) <= h < time(18, 0):
        return 'Tarde'
    elif time(18, 0) <= h < time(23, 59, 59):  # até 23:59
        return 'Noite'
    else:
        return 'Madrugada'

ocorrencias['ocorrencia_turno'] = ocorrencias['ocorrencia_hora'].apply(categoriza_turno)

colunas = ocorrencias.columns.tolist()
colunas.insert(8, colunas.pop(colunas.index('ocorrencia_turno')))
ocorrencias = ocorrencias[colunas]

print('Df tratado:\n', ocorrencias.head(5).to_string())

print('\nFrequência de Turnos: \n', ocorrencias['ocorrencia_turno'].value_counts())

# Salvar Df
ocorrencias.to_csv('ocorrencias_tratados.csv', index=False)