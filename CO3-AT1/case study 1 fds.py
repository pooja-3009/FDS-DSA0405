import statistics

salary = [4, 5, 5, 6, 7, 8, 8, 9, 30]

print("CASE STUDY 1 - Employee Salaries")

mean = statistics.mean(salary)
median = statistics.median(salary)
mode = statistics.multimode(salary)
data_range = max(salary) - min(salary)
variance = statistics.variance(salary)
std_dev = statistics.stdev(salary)

q1 = statistics.median(salary[:4])
q3 = statistics.median(salary[5:])
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = []
for x in salary:
    if x < lower or x > upper:
        outliers.append(x)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Range:", data_range)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Outlier:", outliers)

if outliers:
    print("Best Measure of Central Tendency: Median")
    print("Reason: Median is not affected by the outlier.")
else:
    print("Best Measure of Central Tendency: Mean")