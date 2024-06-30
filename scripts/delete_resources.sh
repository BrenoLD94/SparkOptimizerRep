# deletando o cluster
gcloud dataproc clusters delete cluster-sparkapp --region us-central1

# deletando tabela do Bigquery
bq rm -t PROJECT_ID.DATASET_ID.agg_users

# deleta todos os arquivos do bucket
gsutil -m rm -r gs://BUCKET_NAME/**



