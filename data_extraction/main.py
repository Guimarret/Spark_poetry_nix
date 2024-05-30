import requests
from pyspark.sql import SparkSession
import gzip
import shutil
import io

spark = SparkSession.builder \
    .appName("GHCN Daily Data Example") \
    .getOrCreate() \
    .setMaster("local")

url = "https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/2023.csv.gz"
local_path_gz = "/home/guimas/Documents/spark_nix_poetry/data/2023.csv.gz"
local_path = "/home/guimas/Documents/spark_nix_poetry/data/2023.csv"

response = requests.get(url, stream=True)
with gzip.open(io.BytesIO(response.content), 'rb') as f_in, open(local_path, 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)

df = spark.read.format("csv").option("header", "false").option("inferSchema", "true").load(local_path)

df.show(n=40)