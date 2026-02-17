# Filter for transactions with TotalPrice greater than 200
high_value_transactions = df.filter(df["Total Price"] > 200)
high_value_transactions.show()


# Assuming you want to analyze transactions in the year 2023
filtered_df = df.filter(
    (df["Total Price"] > 200) & 
    (df["Timestamp"].between('2023-01-01', '2023-12-31'))
)
filtered_df.show()