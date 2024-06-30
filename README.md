# Carregando 200 Milhões de linhas usando Pyspark

Vou utilizar o Google Cloud Dataproc para criar um cluster com Apache Spark e processar os dados. Os dados foram extraídos de um dataset público do BigQuery e exportados para um bucket do Google Cloud Storage. Após o processamento, os dados serão armazenados em uma tabela no BigQuery. O objetivo é simular uma tarefa real.

Dataset: bigquery-public-data.stackoverflow
Tabelas: 
    - bigquery-public-data.stackoverflow.badges
    - bigquery-public-data.stackoverflow.post_history
    - bigquery-public-data.stackoverflow.users

## Pré-requisitos:
* Uma conta na Google Cloud

## Estrutura das Pastas
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
│
├── src/ # Código-fonte do projeto
│ ├── main.py # Ponto de entrada principal para o job Spark
│ ├── utils/ # Módulo de propósito geral
│ │ ├── utils.py Funções utilitárias
│ │ ├── transformers.py # transformações de negócio
| 
└── logs/ # Logs de execução


## Como Executar
    Execute no Google Console Cloud

Criar Bucket
Criar tabela no BQ
Criar Cluster
Submeter o job


## Referências

https://github.com/GoogleCloudDataproc/spark-bigquery-connector#properties
