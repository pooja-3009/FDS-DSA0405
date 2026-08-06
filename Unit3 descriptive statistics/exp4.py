import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Employee_Salary_Dataset.csv")

salary_column = df.select_dtypes(include=["number"]).columns[-1]

plt.boxplot(df[salary_column])

plt.title("Salary Box Plot")
plt.ylabel("Salary")

plt.show()

print("Points outside the whiskers are Outliers.")