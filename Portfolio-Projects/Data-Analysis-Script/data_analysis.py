import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
def load_data(file_path):
    """Loads data from a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

# Data summary
def summarize_data(df):
    """Returns basic statistics and info about the DataFrame."""
    print("Data Summary:\n", df.describe())
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nData Types:\n", df.dtypes)

# Data visualization
def plot_distribution(df, column):
    """Plots the distribution of a given column."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], bins=30, kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

# Correlation heatmap
def plot_correlation(df):
    """Plots a heatmap of the correlation matrix."""
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.show()

# Handle missing values
def handle_missing_values(df, method='mean'):
    """Fills missing values using mean, median, or mode."""
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if method == 'mean':
                df[col].fillna(df[col].mean(), inplace=True)
            elif method == 'median':
                df[col].fillna(df[col].median(), inplace=True)
            elif method == 'mode':
                df[col].fillna(df[col].mode()[0], inplace=True)
    return df

if __name__ == "__main__":
    file_path = "data.csv"  # Change this to your file path
    df = load_data(file_path)
    summarize_data(df)
    plot_correlation(df)
    
    # Example usage of plotting distribution
    if 'column_name' in df.columns:
        plot_distribution(df, 'column_name')
