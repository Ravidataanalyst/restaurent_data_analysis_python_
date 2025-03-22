
import pandas as pd
import numpy as np

# Load the dataset 
df = pd.read_csv("C:/Users/RAVI KUMAR C/OneDrive/Desktop/INTERN LEVELS/dataset/dataset intern.csv")


# Descriptive statistics for numerical columns
numerical_columns = df.select_dtypes(include=[np.number]).columns
numerical_stats = df[numerical_columns].describe()

# Mean, median, standard deviation for numerical columns
mean_values = df[numerical_columns].mean()
median_values = df[numerical_columns].median()
std_dev_values = df[numerical_columns].std()

# Distribution of categorical variables
categorical_columns = ['Country Code', 'City', 'Cuisines']
categorical_distribution = {col: df[col].value_counts() for col in categorical_columns}

# Top cuisines and cities with the highest number of restaurants
top_cuisines = df['Cuisines'].value_counts()
top_cities = df['City'].value_counts()

# Display the results
print("Descriptive Statistics for Numerical Columns:")
print(numerical_stats)
print("\nMean Values for Numerical Columns:")
print(mean_values)
print("\nMedian Values for Numerical Columns:")
print(median_values)
print("\nStandard Deviation for Numerical Columns:")
print(std_dev_values)
print("\nDistribution of Categorical Variables:")
for col, distribution in categorical_distribution.items():
    print(f"\n{col} Distribution:")
    print(distribution)
print("\nTop Cuisines:")
print(top_cuisines)
print("\nTop Cities:")
print(top_cities)


