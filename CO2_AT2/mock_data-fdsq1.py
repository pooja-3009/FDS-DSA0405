import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Create sample data
raw_data = {
    "Employee_Name": [" Alice ", "Bob", "Charlie", "Diana", "Evan"],
    "Department": ["HR", "Engineering", "HR", "Engineering", "Marketing"],
    "Salary": [50000, 85000, np.nan, 92000, 60000],
    "Join_Date": [
        "2022-01-15",
        "2021-06-20",
        "2023-03-11",
        "2020-11-01",
        "2024-02-28",
    ],
}

df = pd.DataFrame(raw_data)

print("Raw Data")
print(df)

# Data preprocessing
df["Employee_Name"] = df["Employee_Name"].str.strip()

median_salary = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(median_salary)

df["Join_Date"] = pd.to_datetime(df["Join_Date"])

df["Years_of_Service"] = 2026 - df["Join_Date"].dt.year

print("\nPreprocessed Data")
print(df)

# Aggregation
dept_summary = (
    df.groupby("Department")
    .agg(
        Avg_Salary=("Salary", "mean"),
        Total_Employees=("Employee_Name", "count")
    )
    .reset_index()
)

print("\nDepartment Summary")
print(dept_summary)

# Visualization
sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(1,2,figsize=(14,5))

sns.barplot(
    data=dept_summary,
    x="Department",
    y="Avg_Salary",
    hue="Department",
    ax=axes[0],
    palette="Blues_d",
    legend=False
)

axes[0].set_title("Average Salary by Department")

sns.scatterplot(
    data=df,
    x="Years_of_Service",
    y="Salary",
    hue="Department",
    style="Department",
    s=200,
    ax=axes[1]
)

axes[1].set_title("Salary vs Years of Service")

plt.tight_layout()
plt.show()