

### **1. Importing Necessary Libraries**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```
- **pandas (`pd`)**: Used for handling and analyzing data.
- **numpy (`np`)**: Provides numerical operations and handling missing values.
- **matplotlib.pyplot (`plt`)**: Used for plotting graphs.
- **seaborn (`sns`)**: Enhances matplotlib with better visualizations.

---

### **2. Loading Data from a CSV File**
```python
def load_data(file_path):
    """Loads data from a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)
```
- Reads a CSV file and converts it into a **DataFrame**, a structured way of handling tabular data.

---

### **3. Summarizing the Data**
```python
def summarize_data(df):
    """Returns basic statistics and info about the DataFrame."""
    print("Data Summary:\n", df.describe())  # Shows stats like mean, median, etc.
    print("\nMissing Values:\n", df.isnull().sum())  # Counts missing values in each column
    print("\nData Types:\n", df.dtypes)  # Displays column data types
```
- **`.describe()`**: Gives statistical summary (mean, std, min, max, etc.).
- **`.isnull().sum()`**: Shows missing values per column.
- **`.dtypes`**: Displays the type of data in each column (integer, float, string, etc.).

---

### **4. Plotting a Distribution Graph**
```python
def plot_distribution(df, column):
    """Plots the distribution of a given column."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], bins=30, kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()
```
- Creates a **histogram** to see how data is spread in a given column.
- **`kde=True`** adds a smooth curve to visualize density.
- Useful for understanding how values are distributed.

---

### **5. Plotting a Correlation Heatmap**
```python
def plot_correlation(df):
    """Plots a heatmap of the correlation matrix."""
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.show()
```
- **`df.corr()`** calculates how strongly each numerical column relates to others.
- **Heatmap** helps visualize relationships (e.g., a high correlation means two variables increase/decrease together).

---

### **6. Handling Missing Values**
```python
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
```
- Fills missing values using:
  - **Mean** (average)
  - **Median** (middle value)
  - **Mode** (most frequent value)
- Helps clean data so it can be analyzed properly.

---

### **7. Running the Script**
```python
if __name__ == "__main__":
    file_path = "data.csv"  # Change this to your file path
    df = load_data(file_path)  # Load the CSV file
    summarize_data(df)  # Print summary statistics
    plot_correlation(df)  # Show heatmap of correlations
    
    # Example usage of plotting distribution
    if 'column_name' in df.columns:
        plot_distribution(df, 'column_name')
```
- Runs the script only if executed directly (not imported as a module).
- Loads a CSV file (`data.csv`).
- Summarizes the data.
- Plots a correlation heatmap.
- If a specific column (`column_name`) exists, it plots its distribution.

---

### **What is a CSV File?**
- **CSV (Comma-Separated Values)** is a format for storing tabular data (like a spreadsheet).
- Example:
  ```
  Name, Age, Salary
  Alice, 25, 50000
  Bob, 30, 60000
  ```
- Each row represents a record, and commas separate the values.

---

Let me know if you need any clarification! 🚀
