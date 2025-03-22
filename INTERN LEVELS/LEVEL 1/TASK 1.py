import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

df = pd.read_csv("C:\\Users\\RAVI KUMAR C\\OneDrive\\Desktop\\INTERN LEVELS\\dataset\\dataset intern.csv")

# 1. Identify the number of rows and columns
num_rows, num_columns = df.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

# 2. Check for missing values in each column
missing_values = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# 3. Handle missing values
# Fill missing numerical values with median
for col in df.select_dtypes(include=[np.number]).columns:
    median = df[col].median()
    df[col].fillna(median, inplace=True)

# Fill missing categorical values with mode
for col in df.select_dtypes(include=[object]).columns:
    mode = df[col].mode()[0]
    df[col].fillna(mode, inplace=True)

# 5. Analyze the distribution of the target variable
target_variable = 'Aggregate rating'  # Replace with the actual target variable name
if target_variable in df.columns:
    # Analyze the distribution of the target variable
    target_distribution = df[target_variable].value_counts()
    print("\nDistribution of the target variable:")
    print(target_distribution)

    # Plot the distribution
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=target_variable)
    plt.title('Distribution of the Target Variable')
    plt.xlabel(target_variable)
    plt.ylabel('Frequency')
    plt.show()
else:
    print(f"\nTarget variable '{target_variable}' not found in the dataset.")
