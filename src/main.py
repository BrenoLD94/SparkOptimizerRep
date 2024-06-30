from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.functions import broadcast
from utils import init_spark_session

def main():
    spark = init_spark_session("stackoverflow200M")

    # Define o nome do bucket e os diretórios de origem e destino
    bucket_name = "bucket_name"
    path_dir = 'dataproc/data/stackoverflow'
    destiny_table = "table_path"

    # Seleciona apenas as colunas necessárias (column pruning) dos arquivos Parquet
    post_history = spark.read.parquet(f"gs://{bucket_name}/{path_dir}/post_history/").select("creation_date", "user_id")
    badges = spark.read.parquet(f"gs://{bucket_name}/{path_dir}/badges/").select("name", "user_id")
    users = spark.read.parquet(f"gs://{bucket_name}/{path_dir}/users/").select("id", "display_name", "reputation", "up_votes", "down_votes", "views")

    # Aplica broadcast nos pequenos conjuntos de dados para melhorar a eficiência de join
    badges_broadcast = broadcast(badges)
    users_broadcast = broadcast(users)

    # Reparte o conjunto de dados para evitar problemas de spill e skew
    post_history_repart = post_history.repartition(1024)

    # Cria views temporárias para que possam ser usadas em consultas SQL
    post_history_repart.createOrReplaceTempView("post_history")
    badges_broadcast.createOrReplaceTempView("badges")
    users_broadcast.createOrReplaceTempView("users")

    # Executa uma consulta SQL para calcular as métricas dos usuários principais
    top_users = spark.sql("""
                        SELECT
                            TO_DATE(post.creation_date) AS creation_date,
                            b.name AS badge_name,   
                            u.display_name,
                            SUM(u.reputation) AS reputation,
                            SUM(u.up_votes) AS up_votes,
                            SUM(u.down_votes) AS down_votes,
                            SUM(u.views) AS views
                            
                        FROM post_history post

                        INNER JOIN users u
                        ON post.user_id = u.id
                        
                        INNER JOIN badges b
                        ON u.id = b.user_id
                        
                        GROUP BY 
                            u.display_name,
                            creation_date,
                            badge_name
                    """)
    
    # Escreve os resultados no BigQuery, particionando por data de criação
    top_users.write.format('bigquery') \
        .option('table', destiny_table) \
        .option("temporaryGcsBucket", f"gs://{bucket_name}/dataproc/tmp") \
        .partitionBy("creation_date") \
        .mode("overwrite") \
        .save()


if __name__ == '__main__':
    main()