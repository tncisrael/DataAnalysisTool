import pandas as pd
import matplotlib.pyplot as plt

# Function to generate box plots
def generate_box_plot(csv_file, column_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Generate the box plot for the specified column
    plt.boxplot(df[column_name])
    
    # Add title and labels
    plt.title(f'Box Plot of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Values')
    
    # Show the plot
    plt.show()

# Example usage:
# generate_box_plot("C:\\TNC\\Reservations\\Reservations.csv", "Avg Daily Rate")
