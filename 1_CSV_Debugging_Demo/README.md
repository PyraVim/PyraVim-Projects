# Project 1: CSV Debugging Demo

This project is a practical, hands-on demonstration of debugging and optimizing a common data processing task in Python. It presents a "before and after" scenario, highlighting the ability to transform a fragile, inefficient script into a robust and high-performance one.

## The Scenario

The goal is to process a `sample_sales_data.csv` file to calculate the total price for each order (`quantity * price`) and save the results to a new CSV. However, the sample data contains common real-world problems, and the initial script is not prepared to handle them.

### The Files

1.  **`sample_sales_data.csv`**: A CSV file containing intentional errors:
    
    - A row with a missing `price` value.
        
    - A `price` column with non-numeric text (`"not_a_price"`) and currency symbols (`$`).
        
    - A `quantity` column with a logically invalid negative number.
        
2.  **`buggy_csv_processor.py`**: The "before" script. It's written inefficiently using `iterrows()` and contains no error handling or data validation. **This script is designed to crash.**
    
3.  **`fixed_csv_processor.py`**: The "after" script. This is the professional, client-ready solution. It demonstrates:
    
    - **Performance Optimization**: Replaces slow loops with fast, vectorized pandas operations.
        
    - **Robust Error Handling**: Cleans data (e.g., strips `$` from prices) and handles conversion errors without crashing.
        
    - **Secure Data Validation**: Identifies and removes rows with invalid or nonsensical data (like negative quantities or missing values).
        
    - **Clear Logging**: Prints informative messages about the cleaning process.
        

## How to Run This Demo

1.  **Set up a virtual environment (Recommended):**
    
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
    
    *On Windows, use `venv\Scripts\activate`*
    
2.  **Install dependencies:**
    
    ```
    pip install -r requirements.txt
    ```
    
3.  **Run the main script:** The `fixed_csv_processor.py` script will first attempt to run the buggy process and then the fixed one, allowing you to see the contrast immediately.
    
    ```
    python fixed_csv_processor.py
    ```
    

## Expected Outcome

When you run the script, you will see:

1.  The "Running Buggy CSV Processor" section will start, then print an **\[ERROR\]** message showing that it crashed.
    
2.  The "Running Fixed & Optimized CSV Processor" section will then run, printing **\[INFO\]** messages about the data it cleaned.
    
3.  It will finish with a **\[SUCCESS\]** message.
    
4.  Two new files will be created:
    
    - `buggy_output.csv` (will likely not be created or will be empty because the script crashed).
        
    - `fixed_output.csv` (will contain the correctly processed and cleaned data).
