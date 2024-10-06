# E-commerce Customer Data Analysis

## Project Overview

This project analyzes e-commerce customer behavior using a dataset of purchases, customer demographics, and product categories. The goal is to extract insights on customer preferences, product trends, and churn patterns.

## Project Structure

- **data/**: Contains the raw and cleaned datasets.
- **data_cleaning/**: Python script to clean the raw dataset.
- **data_analysis/**: Jupyter notebook for analyzing and visualizing data.

## Steps

1. Data cleaning: Executed via `data_cleaning/data_cleaning_script.py`.
2. Data analysis and visualization: Executed via `data_analysis/ecommerce_analysis.ipynb`.

## Visualizations

- Total Purchases by Product Category (Bar chart)
- Payment Method Distribution (Pie chart)
- Customer Age Distribution (Histogram)
- Purchases Over Time (Line chart)

## How to Run

- Activate virtual environment:
  ```bash
  source venv/bin/activate
  ```
- Run the cleaning script:
  ```bash
  python data_cleaning/data_cleaning_script.py
  ```
- Launch the Jupyter notebook:
  ```bash
  jupyter notebook
  ```

## Requirements

- pandas
- matplotlib
