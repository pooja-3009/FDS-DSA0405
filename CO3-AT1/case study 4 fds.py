import statistics

orders = [18, 20, 22, 22, 24, 25, 26, 28, 30, 35]

print("CASE STUDY 4 - E-Commerce Orders")

mean = statistics.mean(orders)
median = statistics.median(orders)
mode = statistics.mode(orders)

variance = statistics.variance(orders)
std_dev = statistics.stdev(orders)

cv = (std_dev / mean) * 100

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Coefficient of Variation (CV):", cv, "%")

print("\nInterpretation:")
print("Standard deviation shows how much the daily orders vary from the average.")

if cv < 20:
    print("The order data is Moderately Variable.")
else:
    print("The order data is Highly Variable.")