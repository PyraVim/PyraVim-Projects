# buggy_csv_processor.py
#
# This script is intentionally flawed to demonstrate common issues in data processing.
# It attempts to read sales data, calculate a total for each order, and save the result.
#
# Flaws include:
# 1. Inefficient Looping: Uses df.iterrows(), which is very slow for large datasets.
# 2. No Error Handling: Will crash if data types are incorrect (e.g., price is not a number).
# 3. No Input Validation: Doesn't check for logical errors like negative quantities.
# 4. Unsafe File Handling: Doesn't specify column structure, leading to index errors on malformed rows.

import pandas as pd
import time

def process_buggy_csv(input_file, output_file):
    """
    Reads a CSV, calculates total price for each row, and saves a new CSV.
    This function contains several bugs.
    """
    print("--- Running Buggy CSV Processor ---")
    start_time = time.time()

    # Reading the CSV without handling potential errors.
    df = pd.read_csv(input_file)
    
    # This list will store the results.
    processed_data = []

    # Inefficiently loop through each row. This is a major performance bottleneck.
    for index, row in df.iterrows():
        # This will raise a ValueError if 'price' isn't a clean number.
        price = float(row['price'])
        
        # This will work, but it doesn't check if the quantity makes sense (e.g., > 0).
        quantity = int(row['quantity'])
        
        # Calculate the total for the order.
        total = price * quantity
        
        # Append the result to our list.
        processed_data.append({
            'order_id': row['order_id'],
            'product_name': row['product_name'],
            'total_price': total
        })

    # Convert the list of dictionaries to a new DataFrame.
    processed_df = pd.DataFrame(processed_data)
    
    # Save the result to a new CSV.
    processed_df.to_csv(output_file, index=False)
    
    end_time = time.time()
    print(f"[*] Buggy script finished in {end_time - start_time:.4f} seconds.")
    print(f"[!] Output saved to {output_file}, but it may be incorrect or incomplete due to errors.")


if __name__ == "__main__":
    # This script will crash on the sample data.
    # A client would see an error and not know why.
    try:
        process_buggy_csv('sample_sales_data.csv', 'buggy_output.csv')
    except Exception as e:
        print(f"\n[ERROR] The buggy script crashed! Reason: {e}")
