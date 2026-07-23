import numpy as np

fuel_data=np.genfromtxt(
    r"C:\Users\pooja\OneDrive\Desktop\Fuel_data.csv",
    delimiter=",",
    skip_header=1,
    dtype=str
)

fuel_efficiency=fuel_data[:,6].astype(float)
make=fuel_data[:,7]

average_efficiency=np.mean(fuel_efficiency)

mazda=fuel_efficiency[make=="mazda"]
audi=fuel_efficiency[make=="audi"]

mazda_avg=np.mean(mazda)
audi_avg=np.mean(audi)

percentage=((mazda_avg-audi_avg)/audi_avg)*100

print("Average Fuel Efficiency:",round(average_efficiency,2),"MPG")
print("Mazda Average:",round(mazda_avg,2),"MPG")
print("Audi Average:",round(audi_avg,2),"MPG")
print("Percentage Improvement:",round(percentage,2),"%")