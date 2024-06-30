# Carregando dataset com 200 Milhões de linhas usando Pyspark

Vou utilizar o Google Cloud Dataproc para criar um cluster com Apache Spark e processar os dados. Os dados foram extraídos de um dataset público do BigQuery e exportados para um bucket do Google Cloud Storage. Após o processamento, os dados serão armazenados em uma tabela no BigQuery. O objetivo é simular uma tarefa real.

## Pré-requisitos:
* Uma conta na Google Cloud

## Observação
* Esse código gerará custos. Lembre que cada 1 TB processado o Bigquery cobra 6,25 dólares e com o cluster que criaremos cada hora de execução deve custar cerca de 3,5 dólares. Existe os custos de armazenamento, mas serão bem mais baratos.

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
- Criar o cluster: Abrir o Cloud Shell e executar o código do script `createCluster.sh`. Essa operação levou menos de 5 minutos no meu caso. Se atente que estamos criando um cluster de 4 nós sendo que cada nó tem 16 cores e 64GB e 250GB de memória de disco.

## Conjunto de dados fonte
**Dataset**: 

    `bigquery-public-data.stackoverflow`
    
**Tabelas**:

- `bigquery-public-data.stackoverflow.badges`
- `bigquery-public-data.stackoverflow.post_history`
- `bigquery-public-data.stackoverflow.users` 

Basta abrir as tabelas acima no Bigquery e exportar como parquet especificando as respectivas pastas criadas no Bucket. Os datasets tem uns 120GB aproximadamente.

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
│
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


## Referências

- https://github.com/GoogleCloudDataproc/spark-bigquery-connector#properties
- https://cloud.google.com/dataproc/docs/quickstarts/create-cluster-gcloud
- ![Cloud Shell]([https://www.exemplo.com](https://cloud.google.com/shell/docs/using-cloud-shell?hl=pt-br))
