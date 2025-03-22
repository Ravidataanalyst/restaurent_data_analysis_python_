import pandas as pd
import numpy as np
import folium
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt
import seaborn as sns

# Load the  dataset
df = pd.read_csv('C:\\Users\\RAVI KUMAR C\\OneDrive\\Desktop\\INTERN LEVELS\\dataset\\dataset intern.csv')

# Create a map centered around the average latitude and longitude
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=12)

# Add markers to the map
for _, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=[row['Restaurant ID']]
    ).add_to(m)

# Save the map to an HTML file
m.save('restaurants_map.html')
print("Map have been created as restaurants_map.html")


# Analyze the distribution of restaurants across different cities or countries
city_distribution = df['City'].value_counts()
country_distribution = df['Country Code'].value_counts()

# Plot city distribution
plt.figure(figsize=(10, 5))
sns.barplot(x=city_distribution.index, y=city_distribution.values)
plt.title('Distribution of Restaurants Across Cities')
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45)
plt.show()

# Plot country distribution
plt.figure(figsize=(10, 5))
sns.barplot(x=country_distribution.index, y=country_distribution.values, palette='viridis')
plt.title('Distribution of Restaurants Across Countries')
plt.xlabel('Country Code')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45)
plt.show()

# Correlation between restaurant's location and its rating
correlation_city_rating = df.groupby('City')['Aggregate rating'].mean().reset_index()
correlation_country_rating = df.groupby('Country Code')['Aggregate rating'].mean().reset_index()

print("Average Rating by City:")
print(correlation_city_rating)
print("\nAverage Rating by Country Code:")
print(correlation_country_rating)

# Additional scatter plot for visual analysis
plt.figure(figsize=(10, 5))
sns.scatterplot(data=correlation_city_rating, x='City', y='Aggregate rating', s=100, color='b')
plt.title('City vs. Aggregate Rating')
plt.xlabel('City')
plt.ylabel('Aggregate Rating')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
sns.scatterplot(data=correlation_country_rating, x='Country Code', y='Aggregate rating', s=100, color='b')
plt.title('Country Code vs. Average Rating')
plt.xlabel('Country Code')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.show()



