import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("SampleSuperstore.csv")

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

clean_data = df[(df["Sales"] >= lower) & (df["Sales"] <= upper)]

# Histogram Before
plt.figure(figsize=(6,4))
plt.hist(df["Sales"], bins=20)
plt.title("Histogram Before Removing Outliers")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Histogram After
plt.figure(figsize=(6,4))
plt.hist(clean_data["Sales"], bins=20)
plt.title("Histogram After Removing Outliers")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Box Plot Before
plt.figure(figsize=(5,4))
plt.boxplot(df["Sales"])
plt.title("Box Plot Before Removing Outliers")
plt.show()

# Box Plot After
plt.figure(figsize=(5,4))
plt.boxplot(clean_data["Sales"])
plt.title("Box Plot After Removing Outliers")
plt.show()