# dataset_cleaner.py
#
# This script demonstrates essential data preprocessing techniques for preparing
# a dataset for AI/ML model training. It uses the famous Titanic dataset as an example.
#
# Author: PyraVim
# Version: 1.0
#
# Skills Showcased:
# - Data loading from a URL.
# - Exploratory data analysis with .info() and .isnull().
# - Handling missing values (imputation and dropping columns).
# - Feature engineering to create new, valuable columns.
# - Data type conversion (categorical to numerical).
# - Saving a cleaned, model-ready dataset.

import pandas as pd
import numpy as np

def clean_titanic_dataset(url, output_filename):
    """
    Loads, cleans, and prepares the Titanic dataset for ML model training.
    
    Args:
        url (str): The URL to the raw CSV data.
        output_filename (str): The name for the output cleaned CSV file.
    """
    print("--- Starting AI/ML Dataset Cleaner ---")

    # --- 1. Load Data ---
    try:
        print(f"\n[INFO] Loading dataset from URL: {url}")
        df = pd.read_csv(url)
    except Exception as e:
        print(f"[ERROR] Failed to load data from URL. Reason: {e}")
        return

    print("\n--- 2. Initial Data Analysis (Before Cleaning) ---")
    print("First 5 rows of the raw dataset:")
    print(df.head())
    print("\nSummary of missing values in the raw dataset:")
    # .info() gives a great overview of data types and non-null counts.
    df.info()

    # --- 3. Handle Missing Values ---
    print("\n--- 3. Handling Missing Values ---")

    # Strategy 1: Impute 'Age'.
    # The median is often better than the mean here as it's less sensitive to outliers.
    median_age = df['Age'].median()
    df['Age'] = df['Age'].fillna(median_age)
    print(f"[FIX] Missing 'Age' values filled with median age: {median_age:.2f}")

    # Strategy 2: Impute 'Embarked'.
    # We'll fill the few missing values with the most common port of embarkation (the mode).
    mode_embarked = df['Embarked'].mode()[0]
    df['Embarked'] = df['Embarked'].fillna(mode_embarked)
    print(f"[FIX] Missing 'Embarked' values filled with mode: {mode_embarked}")

    # Strategy 3: Drop 'Cabin' column.
    # The 'Cabin' column has too many missing values to be useful.
    df.drop('Cabin', axis=1, inplace=True)
    print("[FIX] 'Cabin' column dropped due to excessive missing values.")

    # --- 4. Feature Engineering ---
    print("\n--- 4. Feature Engineering ---")

    # We can extract titles (Mr, Mrs, Miss, etc.) from the 'Name' column.
    df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
    # Consolidate rare titles into a single 'Other' category.
    common_titles = ['Mr', 'Miss', 'Mrs', 'Master']
    df['Title'] = df['Title'].replace([title for title in df['Title'].unique() if title not in common_titles], 'Other')
    print("[CREATE] 'Title' column created by extracting from 'Name'.")

    # Drop columns that are no longer needed after engineering.
    df.drop(['Name', 'Ticket', 'PassengerId'], axis=1, inplace=True)
    print("[CLEAN] Dropped 'Name', 'Ticket', and 'PassengerId' columns.")

    # --- 5. Convert Categorical Data to Numerical ---
    print("\n--- 5. Converting Categorical Features to Numbers ---")

    # Models need numbers, not text. We'll convert 'Sex', 'Embarked', and 'Title'.
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1}).astype(int)
    
    # get_dummies creates new columns for each category (one-hot encoding).
    df = pd.get_dummies(df, columns=['Embarked', 'Title'], drop_first=True)
    print("[CONVERT] Converted 'Sex', 'Embarked', and 'Title' to numerical format.")

    # --- 6. Final Data Analysis (After Cleaning) ---
    print("\n--- 6. Final Data Analysis (After Cleaning) ---")
    print("First 5 rows of the cleaned dataset:")
    print(df.head())
    print("\nSummary of the cleaned dataset (no missing values):")
    df.info()

    # --- 7. Save Cleaned Data ---
    try:
        df.to_csv(output_filename, index=False)
        print(f"\n[SUCCESS] Cleaned dataset saved to {output_filename}")
    except IOError as e:
        print(f"\n[ERROR] Could not save the file. Reason: {e}")

    print("\n--- Dataset Cleaner Finished ---")


if __name__ == "__main__":
    # This is the direct link to the raw titanic.csv data file.
    DATA_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    OUTPUT_FILE = "titanic_cleaned.csv"
    clean_titanic_dataset(DATA_URL, OUTPUT_FILE)
