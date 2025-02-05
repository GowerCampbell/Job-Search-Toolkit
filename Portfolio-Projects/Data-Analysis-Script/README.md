# Data Analysis Script

## Overview
This script is designed to help analyze and visualize data from CSV (Comma-Separated Values) files using **Python** and popular libraries like **pandas**, **NumPy**, **matplotlib**, and **seaborn**.

## What is a CSV file?
A **CSV file** is a plain text file that stores data in a tabular format. Each row represents a record, and each column represents a field, separated by commas.

Example:
```
Name, Age, Score
Alice, 25, 85
Bob, 30, 90
Charlie, 22, 78
```
This format is widely used for data storage and exchange.

## Features of This Script
1. **Load Data**: Reads a CSV file into a pandas DataFrame.
2. **Summarize Data**: Displays basic statistics, missing values, and data types.
3. **Visualizations**:
   - Distribution plots for numerical columns.
   - Correlation heatmaps to understand relationships between features.
4. **Handle Missing Values**: Replaces missing data using mean, median, or mode.

## How to Use
### 1. Install Dependencies
Make sure you have Python installed. Install the required libraries using:
```sh
pip install pandas numpy matplotlib seaborn
```

### 2. Run the Script
Save your dataset as `data.csv` in the same directory and execute:
```sh
python data_analysis.py
```

### 3. Customization
- Change the `file_path` variable to your CSV file location.
- Modify the `plot_distribution(df, 'column_name')` function to analyze specific columns.

## Example Usage
If your dataset has a column named `Age`, you can visualize its distribution by calling:
```python
plot_distribution(df, 'Age')
```

## License
This project is open-source under the **MIT License**.

---
🚀 Developed by Gower Campbell


