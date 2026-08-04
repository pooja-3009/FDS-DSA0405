import statistics

response = [120, 125, 128, 130, 132, 135, 140, 145, 150, 300]

print("CASE STUDY 2 - Website Response Time")

mean = statistics.mean(response)
median = statistics.median(response)
data_range = max(response) - min(response)
variance = statistics.variance(response)
std_dev = statistics.stdev(response)

q1 = statistics.median(response[:5])
q3 = statistics.median(response[5:])
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = []
for x in response:
    if x < lower or x > upper:
        outliers.append(x)

print("Mean:", mean)
print("Median:", median)
print("Range:", data_range)
print("Variance:", variance)
print("Standard Deviation:", std_dev)

if mean > median:
    print("Skewness: Right-skewed")
else:
    print("Skewness: Left-skewed")

print("Outlier:", outliers)
print("Median is more useful because it is not affected by the extreme response time (300 ms).")