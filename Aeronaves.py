# 1 - COLETA DE DADOS

# Importar a Biblioteca
import pandas as pd
import  numpy as np

# Ler o arquivo
aeronaves = pd.read_csv('aeronave.csv', sep=';')

# 2 - ANÁLISE EXPLORATÓRIA

# Verificar os registros e tamanhos
print('Tabela:\n',aeronaves.head(5).to_string())
print('\nTotal de Linha e Colunas: ', aeronaves.shape)

# Visão geral dos dados
print('\nTipagem da Tabela Aeronaves: \n', aeronaves.info())
print('\nValores nulos: \n', aeronaves.isnull().sum())
print('\nTotal de valores nulos: ', aeronaves.isnull().sum().sum() )

# Estatística Descritiva
print('\nEstatistica do df: \n', aeronaves.describe().to_string())

print('\nOperador : \n', aeronaves['aeronave_operador_categoria'].value_counts().head(20))
print('\nRegistro : \n', aeronaves['aeronave_registro_categoria'].value_counts().head(20))
print('\nSegmento : \n', aeronaves['aeronave_registro_segmento'].value_counts().head(20))
print('\nTipo de Operação: \n', aeronaves['aeronave_tipo_operacao'].value_counts().head(20))
print('\nDanos \n', aeronaves['aeronave_nivel_dano'].value_counts().head(20))
print('\nDanos \n', aeronaves[['aeronave_tipo_veiculo', 'aeronave_registro_categoria']].value_counts().head(20))

# Excluir colunas desnecessárias
Aeronaves = aeronaves.drop(['aeronave_matricula', 'aeronave_tipo_icao', 'aeronave_pmd_categoria', 'aeronave_operador_categoria', 'aeronave_registro_categoria'], axis=1, inplace=True)

# Ajustar o nome da coluna
aeronaves.rename(columns={'codigo_ocorrencia2': 'codigo_ocorrencia'}, inplace=True)

print('Tabela Tratada:\n',aeronaves.head(5).to_string())

print('\nTotal de Linha e Colunas: ', aeronaves.shape)
# 3 - LIMPEZA DOS DADOS

#Tratar valores duplicados
aeronaves.drop_duplicates()
print('Qtd de registros removendo as duplicadas:', len(aeronaves))

#Excluir Linhas com mais 10 registros nulos
aeronaves = aeronaves.dropna(thresh=10)
print('Qtd total de registros nulos após exclusão:', aeronaves.isnull().sum().sum())

#Tratar valores nulos - Qualitativos
aeronaves.fillna({'aeronave_fabricante': 'Não Informado',
                   'aeronave_modelo': 'Não Informado',
                   'aeronave_motor_tipo': 'Não Informado',
                   'aeronave_voo_origem': 'Não Informado',
                   'aeronave_voo_destino': 'Não Informado',},
                  inplace=True)

# TRATAR OS OUTLIERS
print('\nPMDs zerados:', (aeronaves['aeronave_pmd'] == 0).sum())
print('\nAno zerados:', (aeronaves['aeronave_ano_fabricacao'] == 0).sum())

# excluir linhas com pmd igual a zero
aeronaves = aeronaves.dropna(subset=['aeronave_pmd']) # Remove linhas com NaN em 'aeronave_pmd'
aeronaves = aeronaves[aeronaves['aeronave_pmd'] != 0] # Remove linhas com 'aeronave_pmd' igual a zero

# substituir o ano pela média
contagem_ano = aeronaves['aeronave_ano_fabricacao'].value_counts().sort_index()
print(contagem_ano)

media_sem_outliers = aeronaves[
    (aeronaves['aeronave_ano_fabricacao'] >= 1932) &
    (aeronaves['aeronave_ano_fabricacao'] <= 2023)
]['aeronave_ano_fabricacao'].mean()

# Substituir outliers pela média
aeronaves['aeronave_ano_fabricacao'] = aeronaves['aeronave_ano_fabricacao'].apply(
    lambda x: media_sem_outliers if pd.isna(x) or x < 1932 or x > 2023 else x
)

print('\nTipagem da Tabela Aeronaves: \n', aeronaves.describe().to_string())

print('\nValores nulos: \n', aeronaves.isnull().sum().sum())

# Tratar valores nulos Assentos
aeronaves['aeronave_assentos'] = aeronaves['aeronave_assentos'].fillna(aeronaves['aeronave_assentos'].mean())

print('\nTotal de valores nulos após tratamento: ', aeronaves.isnull().sum().sum() )

#Converter tipos de dados
aeronaves['aeronave_assentos'] = aeronaves['aeronave_assentos'].astype(int)
aeronaves['aeronave_ano_fabricacao'] = aeronaves['aeronave_ano_fabricacao'].astype(int)

# Salvar Df
aeronaves.to_csv('aeronaves_tratados.csv', index=False)
