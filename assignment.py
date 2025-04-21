import pandas as pd

file_path = 'diagnosed_cbc_data_v4.csv'

try:
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Show first few rows
    print("✅ Dataset Loaded Successfully!\n")
    print(df.head())

except FileNotFoundError:
    print(f"❌ File not found. Make sure '{file_path}' exists in your directory.")
except Exception as e:
    print(f"❌ An error occurred: {e}")
