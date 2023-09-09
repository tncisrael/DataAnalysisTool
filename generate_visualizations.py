import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def generate_histograms(df):
    metrics = ['Country', 'Status', 'Channel', 'Special Occasion Mentioned']
    print("Generating histograms...")
    for metric in metrics:
        if metric in df.columns:
            print(f"Processing {metric}...")
            print(f"Unique values in {metric}: {df[metric].unique()}")
            print(f"Value counts:\n{df[metric].value_counts()}")
            sns.histplot(df[metric], kde=False)
            plt.title(f'Histogram of {metric}')
            plt.show()

def generate_boxplots(df):
    metrics = ['Country', 'Status', 'Channel', 'Special Occasion Mentioned']
    print("Generating boxplots...")
    for metric in metrics:
        if metric in df.columns:
            print(f"Processing {metric}...")
            if pd.api.types.is_numeric_dtype(df[metric]):
                sns.boxplot(x=df[metric])
                plt.title(f'Boxplot of {metric}')
                plt.show()
            else:
                print(f"Skipping {metric} as it is not a numeric column.")
