import pandas as pd
df=pd.read_csv("C:/Users/RAVI KUMAR C/OneDrive/Desktop/INTERN LEVELS/dataset/dataset intern.csv")
# Determine the most common price range among all the restaurants
most_common_price_range = df['Price range'].mode()[0]

# Calculate the average rating for each price range
average_rating_by_price_range = df.groupby('Price range')['Aggregate rating'].mean()

# Merge the average ratings with their corresponding colors
price_range_colors = df[['Price range', 'Rating color']].drop_duplicates().set_index('Price range')
average_rating_with_colors = average_rating_by_price_range.to_frame().join(price_range_colors)

# Find the color corresponding to the highest average rating
highest_avg_rating_color = average_rating_with_colors.loc[average_rating_with_colors['Aggregate rating'].idxmax()]['Rating color']


# Output 

print('Most Common Price Range:', most_common_price_range)
print('Average Rating by Price Range:', average_rating_by_price_range)
print(f"Color representing the highest average rating: {highest_avg_rating_color}")


