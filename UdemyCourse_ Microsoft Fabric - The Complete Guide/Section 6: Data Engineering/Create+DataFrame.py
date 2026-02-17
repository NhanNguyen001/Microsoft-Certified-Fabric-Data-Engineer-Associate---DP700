# Create a DataFrame from a collection of tuples
data = [("James", 34, "New York"), ("Anna", 30, "London"), ("Bob", 23, "San Francisco")]

df = spark.createDataFrame(data, schema=["Name", "Age", "City"])
df.show()



display(df)
