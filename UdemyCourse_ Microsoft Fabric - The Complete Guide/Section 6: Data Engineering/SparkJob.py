from pyspark.sql import SparkSession

def main():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("CSV to Parquet Converter") \
        .getOrCreate()

    # Read the CSV file into a DataFrame
    sales = spark.read.format("csv") \
        .option("header", "true") \
        .load("Files/sales/sales.csv")
    # Assuming "Files/sales/sales.csv" is the path where your input CSV file is located.

    # Perform a basic transformation
    # As an example, let's filter rows with sales greater than a certain value.
    # This step is optional and can be customized based on the transformation you need.
    # Here, we're assuming there's a column named "Amount" in the CSV file.
    # Replace "Amount" with the actual column name you wish to filter on and adjust the condition as needed.
    sales_filtered = sales.filter(sales["Total Price"] > 1000)
    
    # Write the transformed DataFrame as a Parquet file, overwriting any existing file
    sales_filtered.write.parquet("Files/sales/parquet/salesnew.parquet", mode="overwrite")
    # Adjust the path "Files/sales/parquet/sales.parquet" as necessary for your output location.

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()
