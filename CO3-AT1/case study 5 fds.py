import statistics

modelA = [2, 3, 3, 4, 4, 5, 5, 6]
modelB = [1, 1, 2, 4, 5, 7, 8, 9]

print("CASE STUDY 5 - Comparing Two Data Science Models")

meanA = statistics.mean(modelA)
meanB = statistics.mean(modelB)

varianceA = statistics.variance(modelA)
varianceB = statistics.variance(modelB)

stdA = statistics.stdev(modelA)
stdB = statistics.stdev(modelB)

print("Model A")
print("Mean Error:", meanA)
print("Variance:", varianceA)
print("Standard Deviation:", stdA)

print("\nModel B")
print("Mean Error:", meanB)
print("Variance:", varianceB)
print("Standard Deviation:", stdB)

if stdA < stdB:
    print("\nModel A has more consistent predictions.")
else:
    print("\nModel B has more consistent predictions.")

if meanA < meanB:
    print("Model A has the lower mean error.")
elif meanB < meanA:
    print("Model B has the lower mean error.")
else:
    print("Both models have the same mean error.")

print("\nExplanation:")
print("A lower mean error alone does not always mean a better model.")
print("Consistency (lower standard deviation) and other performance metrics are also important.")