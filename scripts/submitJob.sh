gcloud dataproc jobs submit pyspark \
    gs://bucket_name/dataproc/job/main.py \
    --bucket=gs://bucket_name/dataproc/tmp \
    --cluster=cluster-sparkapp  \
    --region=us-central1 \
    --py-files=gs://bucket_name/dataproc/job/utils/utils.py,gs://bucket_name/dataproc/job/utils/transformers.py