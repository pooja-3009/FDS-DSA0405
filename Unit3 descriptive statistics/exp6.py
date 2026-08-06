import pandas as pd

# Load dataset
df = pd.read_csv("SampleSuperstore.csv")

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

clean_data = df[(df["Sales"] >= lower) & (df["Sales"] <= upper)]

print("Original Dataset Shape:", df.shape)
print("Cleaned Dataset Shape:", clean_data.shape)

clean_data.to_csv("CleanedSales.csv", index=False)

print("\nCleaned dataset saved as CleanedSales.csv")