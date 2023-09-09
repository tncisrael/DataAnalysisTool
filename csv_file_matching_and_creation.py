import os
import pandas as pd

# Define the directory where your files and subdirectories are located
root_directory = "C:\\TNC"

# List of subdirectories
subdirectories = [
    "Reservations", "Listings", "Apartments", "Expenses", "Guests", 
    "Guest_Messages", "Channels", "Projects", "Tasks", "Inventory", 
    "Vendors", "Hosts", "Competitors", "Reviews", "Amenities", 
    "Software", "Upsells", "Social", "FAQ", "Pricing", 
    "Automations", "Messaging_Strategies"
]

# Function to check and create CSV files
def check_and_create_csv(subdirectory, file_name):
    file_path = os.path.join(root_directory, subdirectory, file_name)
    if not os.path.exists(file_path):
        # Create a new DataFrame with default columns
        df = pd.DataFrame(columns=["Column1", "Column2"])
        
        # Save the DataFrame to a new CSV file
        df.to_csv(file_path, index=False)
        print(f"Created and modified {file_name} in {subdirectory}")

# Example usage:
# for subdirectory in subdirectories:
#     check_and_create_csv(subdirectory, f"{subdirectory}.csv")
