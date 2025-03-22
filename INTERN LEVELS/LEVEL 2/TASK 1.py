import pandas as pd

# Load the dataset
df = pd.read_csv('C:/Users/RAVI KUMAR C/OneDrive/Desktop/INTERN LEVELS/dataset/dataset intern.csv')

# 1. Determine the percentage of restaurants that offer table booking and online delivery
total_restaurants = len(df)
table_booking_count = len(df[df['Has Table booking'] == 'Yes'])
online_delivery_count = len(df[df['Has Online delivery'] == 'Yes'])

percentage_table_booking = (table_booking_count / total_restaurants) * 100
percentage_online_delivery = (online_delivery_count / total_restaurants) * 100

print(f"Percentage of restaurants that offer table booking: {percentage_table_booking:.2f}%")
print(f"Percentage of restaurants that offer online delivery: {percentage_online_delivery:.2f}%")

# 2. Compare the average ratings of restaurants with table booking and those without
average_rating_with_table_booking = df[df['Has Table booking'] == 'Yes']['Aggregate rating'].mean()
average_rating_without_table_booking = df[df['Has Table booking'] == 'No']['Aggregate rating'].mean()

print(f"Average rating of restaurants with table booking: {average_rating_with_table_booking:.2f}")
print(f"Average rating of restaurants without table booking: {average_rating_without_table_booking:.2f}")

# 3. Analyze the availability of online delivery among restaurants with different price ranges
online_delivery_by_price_range = df.groupby('Price range')['Has Online delivery'].value_counts(normalize=True).unstack()

print("Availability of online delivery among restaurants with different price ranges:")
print(online_delivery_by_price_range)

# To visualize the results matplotlib and seaborn is used
import seaborn as sns
import matplotlib.pyplot as plt
online_delivery_by_price_range.plot(kind='bar', stacked=True)
plt.title('Availability of Online Delivery by Price Range')
plt.ylabel('Percentage')
plt.xlabel('Price Range')
plt.xticks(rotation=0)
plt.legend(title='Online Delivery', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

