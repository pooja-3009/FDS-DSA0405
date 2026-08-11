import pandas as pd

# Input data
data = {
    "Customer": ["A", "B", "C", "D", "E", "F"],
    "Age": [25, 30, 22, 45, 35, 28],
    "Total Spending": [60000, 30000, 15000, 70000, 25000, 10000]
}

df = pd.DataFrame(data)

# Create customer segments
def segment(spending):
    if spending >= 50000:
        return "High Spenders"
    elif spending >= 20000:
        return "Medium Spenders"
    else:
        return "Low Spenders"

df["Segment"] = df["Total Spending"].apply(segment)

# Calculate average age
average_age = df.groupby("Segment")["Age"].mean()

print("Customer Segmentation:")
print(df)

print("\nAverage Age of Each Segment:")
print(average_age)