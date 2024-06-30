from pyspark.sql import SparkSession
from pyspark import SparkConf

def init_spark_session(appName):
    '''Inicializa a sessão do spark'''
    spark = SparkSession.builder \
        .appName(appName) \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.executor.instances", 11) \
        .config("spark.executor.cores", "5") \
        .config("spark.executor.memory", "18g") \
        .getOrCreate()
    
    print(SparkConf().getAll())
    spark.sparkContext.setLogLevel("ERROR")
    
    return spark