import numpy as np

house_data = np.array([
    ["H1", 3, 1400, 7500000],
    ["H2", 5, 2200, 12500000],
    ["H3", 4, 1800, 9800000],
    ["H4", 6, 3000, 18500000],
    ["H5", 2, 1100, 5200000]
], dtype=object)

filtered = house_data[house_data[:,1] > 4]

average_price = np.mean(filtered[:,3].astype(int))

print("Houses with more than 4 bedrooms:")
print(filtered)

print("Average Sale Price =", average_price)    