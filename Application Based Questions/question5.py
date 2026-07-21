from sklearn.tree import DecisionTreeClassifier, export_text

X = [
    [45000,720,0],
    [30000,650,1],
    [60000,780,0],
    [28000,620,2],
    [52000,710,1]
]

y = [1,0,1,0,1]

model = DecisionTreeClassifier(criterion="gini")
model.fit(X, y)

income = int(input("Enter Income: "))
credit = int(input("Enter Credit Score: "))
loan = int(input("Enter Existing Loans: "))

prediction = model.predict([[income, credit, loan]])

if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")

print("\nDecision Rules:")
print(export_text(model, feature_names=["Income","CreditScore","ExistingLoans"]))