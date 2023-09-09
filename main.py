from data_import_and_cleaning import import_and_clean_data
from csv_file_matching_and_creation import check_and_create_csv
from generate_visualizations import generate_histograms, generate_boxplots

def check_data_types(df):
    metrics = ['Country', 'Status', 'Channel', 'Special Occasion Mentioned']
    print("Checking data types...")
    for metric in metrics:
        if metric in df.columns:
            print(f"Data type of column {metric}: {df[metric].dtype}")
        else:
            print(f"Column {metric} not found in DataFrame.")

print("Starting the main program...")
print("Importing and cleaning data...")
df = import_and_clean_data("C:\\TNC\\Reservations\\Reservations.csv")
print("Data imported and cleaned.")

# Check data types
check_data_types(df)

# Print DataFrame columns for debugging
print("DataFrame columns:", df.columns)

print("Checking and creating CSV files...")
check_and_create_csv("Reservations", "Reservations.csv")
print("CSV files checked and created.")

print("Generating visualizations...")
generate_histograms(df)
generate_boxplots(df)
print("Visualizations generated.")

print("Main program completed.")
