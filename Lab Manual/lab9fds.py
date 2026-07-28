import pandas as pd

# Read the CSV file
df = pd.read_csv(r"C:\Users\pooja\OneDrive\Desktop\house.csv")

# Average house price for each location
location_price_average = df.groupby("Location")["price"].mean()

# Number of houses with more than 4 bedrooms
more_than_4beds = df[df["beds"] > 4].shape[0]

# Largest house size
largest_sq_feet = df["size"].max()

# Display the results
print("Average House Price for Each Location:")
print(location_price_average)

print("\nNumber of Houses with More Than 4 Bedrooms:", more_than_4beds)

print("Largest House Size:", largest_sq_feet)