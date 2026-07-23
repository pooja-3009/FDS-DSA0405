import numpy as np

sales_data=np.genfromtxt(
    r"C:\Users\pooja\OneDrive\Desktop\Quarterly_Sales.csv",
    delimiter=",",
    skip_header=1,
    dtype=str
)

months=sales_data[:,1]
sales=sales_data[:,4].astype(float)

Q1=0
Q4=0

for i in range(len(months)):
    if months[i] in ["January","February","March"]:
        Q1+=sales[i]
    elif months[i] in ["October","November","December"]:
        Q4+=sales[i]

total_sales=np.sum(sales)

percentage=((Q4-Q1)/Q1)*100

print("Total Sales:",total_sales)
print("Percentage Increase:",round(percentage,2),"%")