import pandas as pd
df = pd.read_json('file.json')  # Path to the json file
df.to_csv('file.csv',index=False)  # New path to the csv file
