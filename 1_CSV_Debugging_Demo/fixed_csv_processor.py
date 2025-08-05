# fixed_csv_processor.py
#
# This script is the corrected and optimized version of buggy_csv_processor.py.
# It demonstrates robust, efficient, and secure coding practices for data processing.
#
# Fixes and Improvements:
# 1. Efficient Operations: Replaces slow df.iterrows() with fast, vectorized pandas operations.
# 2. Robust Error Handling: Uses try-except blocks and data cleaning to handle non-numeric values.
# 3. Secure Input Validation: Checks for logical errors (e.g., negative quantities) and removes invalid data.
# 4. Defensive Programming: Explicitly handles missing data and logs issues without crashing.

import pandas as pd
import time

# Import the function from the other script
from buggy_csv_processor import process_buggy_csv


def clean_price(price):
    """
    Safely converts a price value to a float.
    - Strips non-numeric characters (like '$').
    - Returns None if conversion fails.
    """
    if isinstance(price, str):
        # Remove currency symbols and whitespace
        price = price.replace('$', '').strip()
    try:
        return float(price)
    except (ValueError, TypeError):
        # If conversion fails, it's not a valid price.
        return None

def process_fixed_csv(input_file, output_file):
    """
    Reads sales data, cleans it, calculates totals, and saves the result securely.
    """
    print("\n--- Running Fixed & Optimized CSV Processor ---")
    start_time = time.time()

    try:
        # Read the CSV file safely.
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"[ERROR] Input file not found: {input_file}")
        return

    # --- Data Cleaning and Validation ---

    # 1. Handle missing data: Drop rows where critical columns are empty.
    initial_rows = len(df)
    df.dropna(subset=['order_id', 'quantity', 'price'], inplace=True)
    if len(df) < initial_rows:
        print(f"[INFO] Dropped {initial_rows - len(df)} rows with missing critical data.")

    # 2. Clean 'price' column: Apply our cleaning function.
    # This is a vectorized operation and is extremely fast.
    df['price'] = df['price'].apply(clean_price)
    
    # 3. Secure Input Validation:
    #    - Ensure quantity is a numeric type, coercing errors to NaN (Not a Number).
    #    - Ensure price is numeric after cleaning.
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    
    #    - Remove rows where cleaning or conversion failed (now NaN).
    df.dropna(subset=['quantity', 'price'], inplace=True)
    
    #    - Remove rows with logically incorrect data (e.g., non-positive quantities).
    #      This prevents calculation errors and ensures data integrity.
    invalid_quantity_mask = df['quantity'] <= 0
    if invalid_quantity_mask.any():
        print(f"[INFO] Found and removed {invalid_quantity_mask.sum()} rows with invalid (<= 0) quantities.")
        df = df[~invalid_quantity_mask]

    # Convert quantity to integer type after validation.
    df['quantity'] = df['quantity'].astype(int)

    # --- Calculation ---
    
    # 4. Performance Optimization: Use vectorized calculation.
    # This single line is dramatically faster than looping through the DataFrame.
    df['total_price'] = df['quantity'] * df['price']
    
    # --- Output ---
    
    # Select and reorder columns for the final output.
    output_df = df[['order_id', 'product_name', 'quantity', 'price', 'total_price']].copy()
    
    # Round the total price for clean financial representation.
    output_df['total_price'] = output_df['total_price'].round(2)

    # Save the cleaned and processed data.
    output_df.to_csv(output_file, index=False)
    
    end_time = time.time()
    print(f"[*] Fixed script finished in {end_time - start_time:.4f} seconds.")
    print(f"[SUCCESS] Cleaned data successfully saved to {output_file}")


if __name__ == "__main__":
    # --- The Demonstration ---
    
    # First, run the buggy script to show that it fails.
    # We wrap this in a try...except block so it doesn't crash our main script.
    print("--- Attempting to run the BUGGY script first... ---")
    try:
        process_buggy_csv('sample_sales_data.csv', 'buggy_output.csv')
    except Exception as e:
        print(f"\n[DEMO SUCCESS] The buggy script crashed as expected!")
        print(f"Reason: {e}\n")

    # Then, run the fixed script to show that it works perfectly.
    process_fixed_csv('sample_sales_data.csv', 'fixed_output.csv')
