import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

plt.hist(df["SalePrice"], bins=30)

plt.title("Histogram of House Prices")
plt.xlabel("Sale Price")
plt.ylabel("Frequency")

plt.show()

print("If the histogram has a long tail to the right, it is Right Skewed.")
print("If it is bell-shaped, it is Normally Distributed.")