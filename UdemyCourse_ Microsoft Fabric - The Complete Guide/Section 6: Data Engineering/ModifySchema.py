
df_with_discount = df.withColumn("Discount", 0.0)

from pyspark.sql.functions import lit



df_with_discount = df.withColumn("Discount", lit(0.0))  # Assuming no discount initially
df_with_discount.show()