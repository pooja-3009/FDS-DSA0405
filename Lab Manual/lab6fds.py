import pandas as pd

df=pd.read_csv(r"C:\Users\pooja\OneDrive\Desktop\grocerystore.csv")

total_sales=df["Sales"].sum()

print("Total Sales:",round(total_sales,2))

discount=0.10
tax=0.18

price_after_discount=total_sales-(total_sales*discount)

price_after_tax=price_after_discount+(price_after_discount*tax)

print("Final Amount:",round(price_after_tax,2))