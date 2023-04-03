import pandas as pd
df = pd.read_parquet('file.parquet')  # Path to the parquet file
df.to_csv('file.csv')  # New path to the csv file
