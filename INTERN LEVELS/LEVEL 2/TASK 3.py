import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\RAVI KUMAR C\\OneDrive\\Desktop\\INTERN LEVELS\\dataset\\dataset intern.csv")

# Extract additional features
# Length of the restaurant name
df['restaurant_name_length'] = df['Restaurant Name'].apply(len)

# Length of the address
df['address_length'] = df['Address'].apply(len)

# Create new features by encoding categorical variables
# Assuming 'table_booking' and 'online_delivery' are columns with values like 'Yes' and 'No'
df['has_table_booking'] = df['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else "NO")
df['has_online_delivery'] = df['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else "NO")
# Print the first few rows to check the new features
print(df.head())
