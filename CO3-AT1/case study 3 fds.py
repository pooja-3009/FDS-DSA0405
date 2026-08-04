import statistics

marks = [42, 45, 48, 50, 52, 52, 55, 58, 60, 62, 65, 95]

print("CASE STUDY 3 - Student Performance")

mean = statistics.mean(marks)
median = statistics.median(marks)

q1 = statistics.median(marks[:6])
q2 = median
q3 = statistics.median(marks[6:])

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = []
for x in marks:
    if x < lower or x > upper:
        outliers.append(x)

print("Q1:", q1)
print("Q2 (Median):", q2)
print("Q3:", q3)
print("IQR:", iqr)
print("Outlier:", outliers)
print("Mean:", mean)
print("Median:", median)

if outliers:
    print("Explanation:")
    print("The outlier", outliers[0], "increases the mean,")
    print("while the median remains almost unchanged.")
else:
    print("No outliers found.")