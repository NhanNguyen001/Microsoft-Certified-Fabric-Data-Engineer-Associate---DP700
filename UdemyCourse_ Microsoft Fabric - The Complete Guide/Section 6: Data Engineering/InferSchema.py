# Defining the Schema Manually

schema = """
    TransactionID STRING,
    CustomerID STRING,
    ProductID STRING,
    QuantitySold INT,
    UnitPrice DOUBLE,
    TotalPrice DOUBLE,
    Timestamp STRING
"""

df = spark.read.format("csv").option("header", "true").schema(schema).load("Files/sales/sales.csv")
display(df)

df.dtypes

# Inferring the Schema Automatically

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("Files/sales/sales.csv")
display(df)