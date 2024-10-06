# E-commerce Customer Data Analysis

## Project Overview

This project analyzes e-commerce customer behavior using a dataset of purchases, customer demographics, and product categories. The goal is to extract insights on customer preferences, product trends, and churn patterns.

## Project Structure

- **data/**: Contains the raw and cleaned datasets.
- **scripts/**: Contains Python scripts for cleaning and analyzing the data.
- **notebooks/**: Jupyter notebooks for detailed analysis and visualization.

## Steps

1. **Data Cleaning**:
   - Executed via `scripts/data_cleaning_script.py`.
2. **Data Analysis and Visualization**:
   - Performed in the Jupyter notebook `notebooks/ecommerce_analysis.ipynb`.

## Visualizations

- **Total Purchases by Product Category** (Bar chart)
- **Payment Method Distribution** (Pie chart)
- **Customer Age Distribution** (Histogram)
- **Purchases Over Time** (Line chart)

## How to Run

1. **Set up the environment**:

   - Create and activate a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. **Install the required packages**:

   - Install dependencies listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the cleaning script**:

   - Clean the raw dataset using the provided Python script:
     ```bash
     python scripts/data_cleaning_script.py
     ```

4. **Launch the Jupyter notebook**:
   - For data analysis and visualization:
     ```bash
     jupyter notebook notebooks/ecommerce_analysis.ipynb
     ```

## Requirements

- `pandas`
- `matplotlib`
- `seaborn` (for enhanced visualizations)

---

This README structure reflects the new directory organization and provides clear instructions on setting up, running the project, and what tools are needed.

Let's break down the contents of each CSV and explain what insights can be drawn from them, along with the concept of **churn**.

### 1. **`summary_statistics.csv`**

This CSV provides key summary statistics for the dataset. Here's a breakdown of each row and its significance:

- **Count**: The total number of observations for each variable is 202,404. This indicates the dataset contains information on 202,404 customers.
- **Mean**: The average values of key variables, such as:

  - **Product Price**: \$254.37 (average price of products sold).
  - **Quantity**: On average, each customer purchased 3 items.
  - **Total Purchase Amount**: On average, each customer spent \$2,725.13.
  - **Customer Age**: The average customer age is around 43.93 years.
  - **Returns**: 0.49, which implies nearly 50% of the customers have made at least one return.
  - **Churn**: 0.199, indicating roughly 20% of customers have churned (explained below).

- **Standard Deviation (std)**: Measures variability. For instance, the **Product Price** has a standard deviation of 141.56, showing substantial variation in prices. The **Total Purchase Amount** also shows significant variability.

- **Min, 25%, 50%, 75%, Max**: These values show the distribution of key variables:
  - **Customer Age** ranges from 18 to 70 years.
  - **Product Price** ranges from \$10 to \$500.
  - **Total Purchase Amount** ranges from \$101 to \$5,350, indicating a wide range of spending behavior.
  - **Churn** has a maximum value of 1, meaning customers either churn (1) or do not (0).

### 2. **`top_categories.csv`**

This CSV shows the **total purchase amount** for the top product categories:

- **Books**: \$165,765,436
- **Clothing**: \$165,415,963
- **Electronics**: \$110,525,945
- **Home**: \$109,870,033

**Insights**:

- **Books and Clothing** are the most popular categories by sales, almost equal in terms of revenue generated.
- **Electronics and Home** products contribute a significant amount but are not as popular as Books and Clothing.
- This data helps in understanding consumer preferences and sales distribution. The business can focus on promoting products in these high-performing categories or strategize to boost sales in underperforming categories.

### 3. **`age_churn_summary.csv`**

This CSV breaks down **churn** by age group:

- **Customer Age**: Represents different age groups (18 to 70 years).
- **Churn**: A binary indicator (0 for not churned, 1 for churned).
- **Counts**: The number of customers in each age group who churned (1) or stayed (0).

**Churn** refers to the percentage of customers who stop engaging with the business or stop purchasing products. High churn rates can indicate dissatisfaction or a lack of customer retention strategies.

**Insights**:

- Across most age groups, the number of non-churning customers (0) is consistently higher than those who churn (1).
- The younger age groups (18 to 30) show relatively lower churn compared to the older groups.
- Age groups around the 40s and 50s show slightly higher churn rates, suggesting these groups may need targeted retention strategies.

### Key Insights and Business Relevance

1. **Customer Demographics**:

   - The average customer age is 43.93, and the age range spans from 18 to 70 years. This suggests a diverse age group, though the older age segments (40-70) may need more attention regarding retention since their churn rates are slightly higher.

2. **Churn and Retention**:

   - Around 20% of customers have churned, which could be a focus area for improvement. The business should investigate the reasons behind customer churn and implement strategies such as loyalty programs, personalized marketing, and better customer service to retain customers, particularly in older age brackets.

3. **Product Categories**:

   - Books and Clothing dominate sales, but the business could aim to boost Electronics and Home categories by offering promotions or bundling products. Understanding which products drive revenue can help allocate marketing budgets more effectively.

4. **Returns**:
   - Since around 50% of customers have made returns, the business could investigate why returns are so common. This could be due to issues such as product quality, mismatched expectations, or unclear product descriptions.

### Suggestions to Improve Business

1. **Enhance Retention Strategies**:

   - Since churn is around 20%, improving customer retention is essential. The business could introduce customer loyalty programs, personalized discounts, and better post-purchase services like easy returns or faster shipping to reduce churn.

2. **Targeted Marketing by Age Group**:

   - Focused marketing efforts based on customer age can be effective. For instance, promoting Books and Clothing to younger customers while designing personalized campaigns for older customers could increase engagement.

3. **Optimize Product Offerings**:

   - Since Books and Clothing are top-selling categories, the business could expand its inventory in these areas or launch new, related products to increase revenue further. For underperforming categories (Electronics, Home), promotions and discounts could drive more sales.

4. **Improve Product Returns Process**:
   - With 50% of customers making returns, it’s crucial to analyze the reasons behind returns and address them. Whether it’s improving product quality, adjusting product descriptions, or offering better sizing guides, reducing return rates can boost profitability.

In summary, this data provides valuable insights into customer behavior, product performance, and potential areas for improvement. By analyzing the statistics and addressing key areas such as churn, returns, and targeted marketing, the business can drive growth and improve customer satisfaction.
