import pandas as pd

def import_and_clean_data(file_path):
    # Import the data
    df = pd.read_csv(file_path)
    
    # Print the first few rows of the DataFrame for debugging
    print("First few rows of the DataFrame:")
    print(df.head())
    
    # Perform data cleaning here
    # For example, remove any rows with missing values in specific columns
    # df.dropna(subset=['Column1', 'Column2'], inplace=True)
    
    return df
