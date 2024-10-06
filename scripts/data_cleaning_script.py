import pandas as pd

# Load dataset in chunks for memory efficiency
chunk_size = 50000
data_chunks = []
for chunk in pd.read_csv('data/ecommerce_customer_data_custom_ratios.csv', chunksize=chunk_size):
    data_chunks.append(chunk)

df = pd.concat(data_chunks, axis=0)

# Handle missing values
df_cleaned = df.dropna()

# Ensure you're assigning with .loc to avoid the SettingWithCopyWarning
df_cleaned.loc[:, 'Purchase Date'] = pd.to_datetime(df_cleaned['Purchase Date'])

# Remove duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Save the cleaned dataset
df_cleaned.to_csv('data/ecommerce_cleaned_data.csv', index=False)
