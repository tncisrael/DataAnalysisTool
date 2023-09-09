import pandas as pd
import matplotlib.pyplot as plt

# Function to generate histograms
def generate_histogram(csv_file, column_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Generate the histogram for the specified column
    plt.hist(df[column_name], bins=10, alpha=0.5, color='g')
    
    # Add title and labels
    plt.title(f'Histogram of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    
    # Show the plot
    plt.show()

# Example usage:
# generate_histogram("C:\\TNC\\Reservations\\Reservations.csv", "Avg Daily Rate")
