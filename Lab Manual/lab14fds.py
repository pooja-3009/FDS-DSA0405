import pandas as pd

data = {
    'Customer': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'Age': [25, 30, 25, 35, 30, 25, 40]
}

df = pd.DataFrame(data)

frequency = df['Age'].value_counts().sort_index()

print("Frequency Distribution of Ages:")
print(frequency)