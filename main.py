# Importar a Biblioteca
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Ler o arquivo
aeronaves = pd.read_csv('aeronaves_tratados.csv')
fatores = pd.read_csv('fatores_tratados.csv')
tipo_ocorrencias = pd.read_csv('tipos_ocorrencias_tratados.csv')
ocorrencias = pd.read_csv('ocorrencias_tratados.csv')
recomendacao = pd.read_csv('recomendacao_tratados.csv')

print('Tabela Aeronaves:\n',aeronaves.head(5).to_string())
print('Tabela Fatores:\n',fatores.head(5).to_string())
print('Tabela Tipos de Ocorrencia:\n',tipo_ocorrencias.head(5).to_string())
print('Tabela Ocorrencias:\n',ocorrencias.head(5).to_string())
print('Tabela Recomendações:\n',recomendacao.head(5).to_string())

# Análises

# Acidentes por turno e ano
acidentes_por_ano_turno = ocorrencias.groupby(['ocorrencia_ano', 'ocorrencia_turno']).size().reset_index(name='total_acidentes')
tabela_pivot = acidentes_por_ano_turno.pivot(index='ocorrencia_ano', columns='ocorrencia_turno', values='total_acidentes').fillna(0)

print(tabela_pivot)

# Acidentes por ano
print('\nFrequencia por ano : \n', ocorrencias['ocorrencia_ano'].value_counts().sort_index(ascending=False))
x = ocorrencias['ocorrencia_ano'].value_counts().index # gerar o index no eixo x
y = ocorrencias['ocorrencia_ano'].value_counts().values # gerar os valores no eixo y

plt.figure(figsize=(10,6))
plt.bar( x, y,color='#60aa65')
plt.title('Frequência de Acidentes por Ano')
plt.ylabel('Frequência')
plt.show()

# Acidentes por estado
print('\nFrequencia por estado: \n', ocorrencias['ocorrencia_uf'].value_counts().head(10))

x = ocorrencias['ocorrencia_uf'].value_counts().index # gerar o index no eixo x
y = ocorrencias['ocorrencia_uf'].value_counts().values # gerar os valores no eixo y

plt.figure(figsize=(10,6))
plt.bar( x, y,color='#60aa65')
plt.title('Frequência de Acidentes por Estado')
plt.ylabel('Frequência')
plt.show()

# Classificação das Ocorrencias por estado
tabela = ocorrencias.groupby(['ocorrencia_uf', 'ocorrencia_classificacao']).size().reset_index(name='total')
tabela_pivot = tabela.pivot(index='ocorrencia_uf', columns='ocorrencia_classificacao', values='total').fillna(0).astype(int)

print(tabela_pivot)

# Acidentes por tipo de aeronave
numeros_absolutos = aeronaves['aeronave_tipo_veiculo'].value_counts()
frequencia = aeronaves['aeronave_tipo_veiculo'].value_counts(normalize=True)*100
tabela = pd.DataFrame({
    'quantidade': numeros_absolutos,
    'percentual (%)': frequencia.round(2)
})

print('\nFrequencia por tipo de aeronave : \n', tabela)

# Frequencia dos ano de fabricação
print('\nFrequencia do ano de fabricação : \n', aeronaves['aeronave_ano_fabricacao'].value_counts())

plt.figure(figsize=(10,6))
sns.kdeplot(aeronaves['aeronave_ano_fabricacao'], fill=True, color='#863e9c')
plt.title('Ano de Fabricação das Aeronaves')
plt.show()

#Correlação entre Pmd e Assentos
print('\nCorrelação: \n', aeronaves[['aeronave_pmd', 'aeronave_assentos']].corr())

# Frequencia dos Tipos de Ocorrencia
print('\nFrequencia do tipo de ocorrencia : \n', tipo_ocorrencias['ocorrencia_tipo'].value_counts().head(10))

