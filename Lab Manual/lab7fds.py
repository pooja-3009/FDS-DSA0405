import pandas as pd

df=pd.read_csv(r"C:\Users\pooja\OneDrive\Desktop\order_data.csv")

total_orders=df.groupby("Full Name")["Order Count"].sum()

avg_order=df.groupby("Items")["Order Total"].mean()

earliest=df["Order"].min()

latest=df["Order"].max()

print("Total Orders")
print(total_orders)

print("\nAverage Order Total")
print(avg_order)

print("\nEarliest Order:",earliest)
print("Latest Order:",latest)