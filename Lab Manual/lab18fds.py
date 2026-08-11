import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Given data
age = [23, 23, 27, 27, 39, 41, 47, 49, 50,
       52, 54, 54, 56, 57, 58, 59, 60, 61]

fat = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2,
       34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

df = pd.DataFrame({
    "Age": age,
    "%Fat": fat
})

# Mean, Median and Standard Deviation
print("Mean:")
print(df.mean())

print("\nMedian:")
print(df.median())

print("\nStandard Deviation:")
print(df.std())

# Boxplots
df.boxplot(column=["Age", "%Fat"])
plt.title("Boxplot of Age and Body Fat")
plt.show()

# Scatter plot
plt.scatter(df["Age"], df["%Fat"])
plt.xlabel("Age")
plt.ylabel("% Body Fat")
plt.title("Age vs Body Fat")
plt.show()

# Q-Q plots
plt.figure()
stats.probplot(df["Age"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Age")
plt.show()

plt.figure()
stats.probplot(df["%Fat"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Body Fat")
plt.show()