import pandas as pd

# Load the cleaned dataset
df_cleaned = pd.read_csv('data/ecommerce_cleaned_data.csv')

# Ensure that data is loaded successfully
if df_cleaned.empty:
    print("Data loading error: The dataset is empty.")
else:
    print("Dataset loaded successfully.\n")

# Summary statistics
print("Summary Statistics:\n")
print(df_cleaned.describe())

# Group by Customer Age and Churn for analysis
print("\nGrouped by Customer Age and Churn:\n")
age_churn_summary = df_cleaned.groupby(['Customer Age', 'Churn']).size()
print(age_churn_summary)

# Top product categories by total purchase amount
print("\nTop Product Categories by Total Purchase Amount:\n")
top_categories = df_cleaned.groupby('Product Category')['Total Purchase Amount'].sum().sort_values(ascending=False)
print(top_categories)

# Save the analysis results
df_cleaned.describe().to_csv('data/output/summary_statistics.csv')
age_churn_summary.to_csv('data/output/age_churn_summary.csv')
top_categories.to_csv('data/output/top_categories.csv')