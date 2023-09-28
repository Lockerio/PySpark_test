from pyspark.sql import SparkSession

from get_data import get_joined_dataframes

spark = SparkSession.builder.getOrCreate()

product_df = spark.read.option("header", "true").csv("data/Product.csv")
category_df = spark.read.option("header", "true").csv("data/Category.csv")
product_category_df = spark.read.option("header", "true").csv("data/Product_Category.csv")


result_df = get_joined_dataframes(product_df, category_df, product_category_df)

result_df.show(n=result_df.count(), truncate=False)
