# Carregando dataset com 200 Milhões de linhas usando Pyspark

Neste tutorial, usaremos o Google Cloud Dataproc para criar um cluster com Apache Spark e processar um grande volume de dados. Os dados foram extraídos de um dataset público no BigQuery e exportados para um bucket do Google Cloud Storage. Após o processamento, os dados serão armazenados em uma tabela no BigQuery. O objetivo é simular uma tarefa real de processamento de dados em larga escala.

## Pré-requisitos:
* Uma conta na Google Cloud

## Observação
__Custos__: Este procedimento gerará custos. O BigQuery cobra $6,25 por 1 TB processado. O cluster Dataproc que criaremos terá um custo aproximado de $3,50 por hora de execução. Além disso, haverá custos de armazenamento, que são mais baixos.

## Preparando o ambiente
- Criar estrutura de "pastas" no bucket. Eu segui a estrutura
```plaintext
bucket_name/
└── dataproc/
    ├── data/
    │   └── stackoverflow/
    │       ├── badges/
    │       ├── post_history/
    │       └── users/
    ├── job/
    │   ├── main.py
    │   └── utils/
    │       ├── transformers.py
    │       └── utils.py
    └── tmp/
```
- Criar tabela no BigQuery: Basta executar o código do script `create_bq_table.sql` no BigQuery.
- Criar o cluster: Abra o Google Cloud Shell e execute o script createCluster.sh. A criação do cluster levou menos de 5 minutos no meu caso. Certifique-se de que o cluster possui 4 nós, cada um com 16 núcleos, 64 GB de memória e 250 GB de disco.

## Conjunto de dados fonte
**Dataset**: 

    `bigquery-public-data.stackoverflow`
    
**Tabelas**:

- `bigquery-public-data.stackoverflow.badges`
- `bigquery-public-data.stackoverflow.post_history`
- `bigquery-public-data.stackoverflow.users` 

Abra as tabelas acima no BigQuery e exporte-as como arquivos Parquet, especificando as respectivas pastas criadas no bucket. Os datasets têm aproximadamente 120 GB no total.

## Estrutura das Pastas
```plaintext
project-root/
│
├── README.md # Documentação do projeto
├── .gitignore # Arquivos e pastas a serem ignorados pelo Git
│
├── config/ # Arquivos de configuração
│
├── notebooks/ # Notebooks Jupyter para experimentação
│ ├── exploration.ipynb # Notebook de exploração
│
├── scripts/ # Scripts de submissão, execução e criação do cluster
│ ├── createCluster.sh # Script para criar o cluster
| ├── submitJob.sh # script para enviar o job para o cluster
| ├── create_bq_table.sql # sql para criar tabela no Bigquery
│ ├── delete_resources.sh # script para deletar os recursos
|
├── src/ # Código-fonte do projeto
│ ├── main.py # Ponto de entrada principal para o job Spark
│ ├── utils/ # Módulo de propósito geral
│ │ ├── utils.py Funções utilitárias
│ │ ├── transformers.py # transformações de negócio
| 
└── logs/ # Logs de execução
```
    
## Como Executar
    Execute o script `submitJob.sh` no Google Console Cloud. Esse job executou em 13 minutos

## Deletando os recursos
    Basta executar o script `delete_resources.sh` no cloud shell. Qualquer erro basta excluir via console gráfica. 

## Referências

- https://github.com/GoogleCloudDataproc/spark-bigquery-connector#properties
- https://cloud.google.com/dataproc/docs/quickstarts/create-cluster-gcloud
- ![Cloud Shell]([https://www.exemplo.com](https://cloud.google.com/shell/docs/using-cloud-shell?hl=pt-br))
