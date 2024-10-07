# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load the cleaned data
data = pd.read_csv('../data/cleaned_data.csv')

# Define features and target (Churn)
X = data.drop('Churn', axis=1)
y = data['Churn']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate model accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Churn Prediction Accuracy: {accuracy * 100:.2f}%')

# Save the churn prediction model
joblib.dump(model, '../models/churn_prediction_model.pkl')
print("Churn prediction model saved as churn_prediction_model.pkl")
