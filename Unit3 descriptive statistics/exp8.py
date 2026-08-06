import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Iris.csv")

print("Dataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDescriptive Statistics:")
print(df.describe())

# Histograms
df.hist(figsize=(10, 8))
plt.show()

# Box Plots
df.boxplot(figsize=(10, 6))
plt.show()

# Detect and Remove Outliers
numeric_columns = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]

clean_data = df.copy()

for col in numeric_columns:
    Q1 = clean_data[col].quantile(0.25)
    Q3 = clean_data[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    clean_data = clean_data[
        (clean_data[col] >= lower) &
        (clean_data[col] <= upper)
    ]

print("\nCleaned Dataset Shape:", clean_data.shape)

clean_data.to_csv("Cleaned_Iris.csv", index=False)

print("Cleaned dataset saved as Cleaned_Iris.csv")