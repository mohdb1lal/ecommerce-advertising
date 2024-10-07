# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Load the cleaned data
data = pd.read_csv('../data/cleaned_data.csv')

# Define features and target (Total Purchase Amount)
X = data.drop('Total Purchase Amount', axis=1)
y = data['Total Purchase Amount']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error for Purchase Amount Prediction: {mse:.2f}')

# Save the purchase amount prediction model
joblib.dump(model, '../models/purchase_amount_model.pkl')
print("Purchase amount model saved as purchase_amount_model.pkl")
