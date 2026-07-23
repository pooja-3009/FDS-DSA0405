import numpy as np

house_data=np.loadtxt(
    r"C:\Users\pooja\OneDrive\Desktop\House_data.csv",
    delimiter=",",
    skiprows=1
)

houses_more_than_4=house_data[house_data[:,1]>4]

average_price=np.mean(houses_more_than_4[:,5])

print("Average Price:",round(average_price,2))