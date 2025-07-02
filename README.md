# 📊 Panorama de Acidentes Aéreos

## ✨ Descrição do Projeto
Este repositório apresenta um painel interativo (dashboard) desenvolvido com o objetivo de explorar e analisar dados sobre acidentes aéreos no Brasil. A ferramenta permite uma visão abrangente sobre padrões, causas, fases críticas do voo e características das aeronaves envolvidas, apoiando decisões baseadas em dados no setor da aviação.

## 🎯 Objetivo
Oferecer uma plataforma visual e interativa para análise de acidentes aéreos, facilitando a identificação de tendências, fatores contribuintes e áreas de maior risco operacional.

## 🧩 Principais Funcionalidades
O dashboard é dividido em seções que abordam diferentes dimensões dos dados:

- Evolução Anual dos Acidentes:
análise da série histórica de acidentes ao longo dos anos.

- Fase da Operação no Momento do Acidente:
identifica as fases do voo com maior incidência de acidentes (decolagem, cruzeiro, pouso etc).

- Distribuição Geográfica por Estado:
mapa interativo que mostra os estados brasileiros com maior número de ocorrências.

- Classificação dos Acidentes:
treemap das principais causas ou categorias dos acidentes (ex: falha técnica, erro humano).

- Fatores Contribuintes:
análise de fatores humanos, operacionais e técnicos que influenciam os acidentes.

- Categoria Operacional:
distribuição por tipo de operação: instrução, táxi aéreo, aviação regular, entre outros.

- Número de Motores da Aeronave:
correlação entre a complexidade da aeronave e frequência de acidentes.

- Nível de Dano da Aeronave:
gravidade dos acidentes: leve, substancial, total, etc.

## 🔍 Análise Exploratória de Dados
A Análise Exploratória de Dados (AED) teve como objetivo compreender as principais características do conjunto de dados e identificar padrões, tendências e possíveis anomalias que pudessem impactar as etapas posteriores do projeto. Inicialmente, realizamos a limpeza dos dados onde avaliei a base de dados, verifique os tamanhos e tipos, chquei e substitui/exclui valores nulos, convertir tipos de dados, tratei dados duplicados e transformei a varíavel horário em categorias. Todas essas etapas foram realizadas no arquivo tratamento_dados.py.

Em seguida, segui com as estatísticas descritivas (como média, mediana e desvio padrão), e realizei análises para responder as perguntas geradas a apartir do problema central. Para isso, utilizei gráficos de barras, pizzas e mapa de calor para visualizar a distribuição das variáveis numéricas e categóricas. Análises de correlação também foram realizadas para entender o relacionamento entre as variáveis, auxiliando na seleção de atributos relevantes para modelos preditivos. Todas essas etapas foram realizadas no arquivo xxxxxxx

A análise dos dados revelou padrões importantes sobre a dinâmica dos acidentes aéreos no Brasil:

- Evolução Temporal: Entre 2014 e 2017, houve uma queda no número de acidentes, mas 2023 apresentou um aumento expressivo (1.421 casos), exigindo investigação aprofundada sobre possíveis causas, como mudanças regulatórias, volume de voos ou condições climáticas.

- Fases Críticas de Voo: Pouso e decolagem concentram a maior parte dos acidentes, reforçando a importância de treinamentos específicos e atenção à infraestrutura. A incidência relevante durante o cruzeiro indica falhas que podem ocorrer mesmo em voo estabilizado.

- Distribuição Geográfica: Estados com maior atividade aérea, como São Paulo e Rio de Janeiro, concentram mais acidentes. Isso sugere correlação com o volume de voos, destacando a necessidade de ações regionais focadas.

- Classificação dos Acidentes: Falhas de motor em voo e perda de controle são as causas mais comuns, evidenciando a importância da manutenção rigorosa e treinamento para resposta a emergências.

- Fatores Contribuintes: Fatores humanos como julgamento de pilotagem e aplicação de comandos lideram as causas, reforçando a urgência de programas de capacitação, simulação e cultura de segurança organizacional.

- Perfil da Aeronave: Aeronaves privadas e monomotores aparecem com maior frequência em acidentes, indicando vulnerabilidades específicas nesse segmento, possivelmente ligadas à menor fiscalização e experiência dos operadores.

- Gravidade dos Acidentes: Apesar de muitos casos resultarem em danos leves ou nenhum, a proporção significativa de danos substanciais ou destruição reforça o custo humano e material envolvido.

![image](https://github.com/user-attachments/assets/9910db52-17fd-4c5c-b7f3-251978518305)
![image](https://github.com/user-attachments/assets/32af7306-e8f9-4e56-8cac-12c2276588bf)

## Ferramentas Utilizadas

- Limpeza e Tratamento dos dados:

  - Python

- Visualização de dados:

  - Looker Studio - [link](https://lookerstudio.google.com/reporting/590d8596-d905-4608-9e7b-59194f0c1dd7)


## 💡 Insights Obtidos

- Aumento Crítico em 2023:
  
O crescimento expressivo de acidentes em 2023 exige uma investigação detalhada. É necessário avaliar se houve aumento proporcional no volume de voos ou se a taxa de acidentes por operação realmente cresceu, considerando fatores como mudanças regulatórias, condições meteorológicas extremas ou introdução de novas aeronaves.

- Fases de Maior Risco:
  
As fases de pouso e decolagem concentram a maior parte dos acidentes, reforçando sua natureza crítica. Isso destaca a necessidade de treinamentos específicos, manutenção dos sistemas de aproximação e melhorias na infraestrutura aeroportuária.

- Fatores Humanos como Causa Predominante:
  
"Julgamento de pilotagem" e "Aplicação de comandos" são os fatores mais associados aos acidentes, sinalizando falhas na formação, avaliação e reciclagem de pilotos. Estratégias de treinamento baseadas em simulação e decisão sob pressão devem ser prioridade.

- Vulnerabilidades na Aviação Privada:
  
Aeronaves privadas lideram em número de acidentes, sugerindo menor controle operacional, deficiência em manutenção ou falhas nos processos de fiscalização. Isso indica a necessidade de reforço regulatório e campanhas de conscientização para operadores não comerciais.

- Manutenção Deficiente como Causa Relevante:
  
A alta incidência de falhas de motor e mau funcionamento de componentes indica que práticas de manutenção preventiva precisam ser mais rigorosas, especialmente em aeronaves com menor redundância (monomotor e bimotor).

- Acidentes em Estados com Maior Tráfego:
  
A concentração de acidentes em regiões mais desenvolvidas economicamente pode estar associada ao maior volume de operações. Contudo, é essencial avaliar se a taxa de acidentes nessas áreas está acima do esperado, para justificar ações de fiscalização direcionada.

- Gravidade dos Acidentes e Potenciais Riscos Futuros:
  
Embora muitos acidentes causem danos leves ou nenhum, os casos substanciais ou com destruição indicam riscos graves. Acidentes de menor impacto não devem ser subestimados, pois podem antecipar falhas mais críticas no futuro.

- Cultura Organizacional e Gestão Operacional:
  
Fatores como "Supervisão gerencial" e "Planejamento de voo" reforçam que a segurança também depende de uma cultura organizacional forte. Políticas internas, comunicação de risco e auditorias regulares são essenciais para mitigar falhas sistêmicas.

## 🗂️ Fontes dos dados
- Descrição:
  
  Repositório, em português, inclui as ocorrências aeronáuticas notificadas ao CENIPA (Centro de Investigação e Prevenção de Acidentes Aeronáuticos) no período de 2014 a 2023 ocorridas em solo brasileiro.

- Tipo de dados:
  
  Estruturado (CSV), formato tabular com colunas.

- Métodos de acesso:
  
  Download diretamente via Kaggle (.csv) após autenticação e importado em Python (pandas).
