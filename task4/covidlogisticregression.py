import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

data = {
    'age': [25, 45, 60, 35, 70, 55, 40, 80, 30, 65],
    'diabetes': [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    'hypertension': [0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    'death': [0, 0, 1, 0, 1, 0, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[['age', 'diabetes', 'hypertension']]
y = df['death']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

new_patient = [[68, 1, 1]] 
prediction = model.predict(new_patient)
probability = model.predict_proba(new_patient)

print("\nPrediction:")
print("Death Risk:", prediction[0])
print("Probability:", probability[0])