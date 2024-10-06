import pandas as pd

# Load the cleaned dataset
df_cleaned = pd.read_csv('data/ecommerce_cleaned_data.csv')

# Summary statistics
print(df_cleaned.describe())

# Group by Customer Age and Churn for analysis
age_churn_summary = df_cleaned.groupby(['Customer Age', 'Churn']).size()
print(age_churn_summary)

# Top product categories by total purchase amount
top_categories = df_cleaned.groupby('Product Category')['Total Purchase Amount'].sum().sort_values(ascending=False)
print(top_categories)
