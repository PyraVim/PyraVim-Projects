# Project 3: Dataset Cleaner for AI/ML

This project demonstrates the critical process of data cleaning and preprocessing, which is a foundational step in any Machine Learning or Data Science workflow. It takes the raw Titanic dataset and transforms it into a clean, model-ready format.

## Description

The `dataset_cleaner.py` script downloads the Titanic dataset, performs a series of cleaning and feature engineering operations, and saves the result. This process is vital for improving the accuracy and reliability of AI/ML models.

The script prints a "before and after" summary to the console, clearly showing the impact of each data transformation.

### Key Data Cleaning & Preprocessing Steps:

- **Handles Missing Values**:
    
    - **Imputation**: Fills missing `Age` values with the dataset's median age and missing `Embarked` values with the most common port.
        
    - **Column Removal**: Drops the `Cabin` column, as it contains too many missing entries to be useful.
        
- **Feature Engineering**:
    
    - Creates a new `Title` feature (e.g., Mr, Mrs, Miss) by extracting it from the `Name` column, providing a potentially more predictive feature than the full name.
        
    - Drops original columns like `Name` and `Ticket` that are not useful for modeling.
        
- **Data Conversion**:
    
    - Converts categorical features like `Sex`, `Embarked`, and the new `Title` column into a numerical format using mapping and one-hot encoding (`get_dummies`), which is required by most machine learning algorithms.
- **Output**:
    
    - Saves the final, clean dataset to `titanic_cleaned.csv`.

## How to Run This Project

1.  **Navigate to this directory:**
    
    ```
    cd 3_Dataset_Cleaner_for_AI_ML
    ```
    
2.  **Set up a virtual environment (Recommended):**
    
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
    
    *On Windows, use `venv\Scripts\activate`*
    
3.  **Install dependencies:**
    
    ```
    pip install -r requirements.txt
    ```
    
4.  **Run the cleaner script:** The script will download the data, process it, and save the output.
    
    ```
    python dataset_cleaner.py
    ```
    
5.  **Check the output:** A new file named `titanic_cleaned.csv` will be created. This file contains the structured, cleaned data ready for model training.
