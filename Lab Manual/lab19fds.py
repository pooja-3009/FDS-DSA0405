import pandas as pd

# Input data
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard", "Mouse", "Monitor", "Printer"],
    "Quantity Sold": [5, 10, 8, 15, 20, 25, 7, 4],
    "Unit Price": [50000, 20000, 15000, 2000, 1000, 500, 12000, 18000]
}

df = pd.DataFrame(data)

# Calculate Total Sales
df["Total Sales"] = df["Quantity Sold"] * df["Unit Price"]

# Product-wise total sales
product_sales = df.groupby("Product")["Total Sales"].sum()

# Calculate profit (20%)
product_profit = product_sales * 0.20

# Display product sales
print("Total Sales for Each Product:")
print(product_sales)

# Overall sales and profit
overall_sales = df["Total Sales"].sum()
overall_profit = overall_sales * 0.20

print("\nOverall Sales:", overall_sales)
print("Overall Profit:", overall_profit)

# Top 5 profitable products
top5 = product_profit.sort_values(ascending=False).head(5)

print("\nTop 5 Profitable Products:")
print(top5)