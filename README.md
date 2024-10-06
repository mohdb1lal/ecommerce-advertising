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
