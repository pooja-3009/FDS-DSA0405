import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv(r"C:\Users\pooja\OneDrive\Desktop\Sales_data.csv")

# Calculate total sales for each month
monthly_sales = df.groupby("Month_sales")["Price"].sum()

# Line Graph
plt.figure(figsize=(8,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Bar Graph
plt.figure(figsize=(8,5))
plt.bar(monthly_sales.index, monthly_sales.values)
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()