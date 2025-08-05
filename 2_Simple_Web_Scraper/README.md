# Project 2: Secure & Ethical Web Scraper

This project demonstrates the ability to build a robust web scraper that extracts data from the web while adhering to ethical and security best practices.

## Description

`web_scraper.py` is a Python script that systematically browses the catalogue of [http://books.toscrape.com](http://books.toscrape.com "null"), a website designed for scraping practice. It extracts the title and price of every book available across all pages of the site and saves the collected data into a clean `books.csv` file.

## Key Features & Skills Demonstrated

This script showcases more than just basic scraping; it highlights a professional approach to web automation:

- **Ethical Rate Limiting**: A `1-second` delay is implemented between HTTP requests to avoid overwhelming the server, a crucial practice for responsible scraping.
    
- **Security-Minded Headers**: The script uses a common browser `User-Agent` string to identify its traffic, preventing it from being instantly blocked as a low-quality bot.
    
- **Robust Error Handling**: The code is wrapped in `try...except` blocks to gracefully handle network issues (e.g., connection failures, timeouts) and parsing errors (e.g., malformed HTML), ensuring the script runs to completion without crashing.
    
- **Automated Pagination**: The scraper intelligently finds and follows the "next" page link, allowing it to traverse the entire multi-page catalogue automatically.
    
- **Structured Data Output**: Utilizes the `pandas` library to structure the scraped data and export it into a universally compatible CSV format, ready for analysis.
    

## How to Run This Project

1.  **Navigate to this directory:**
    
    ```
    cd 2_Simple_Web_Scraper
    ```
    
2.  **Set up a virtual environment (Recommended):**
    
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
    
    *On Windows, use `venv\Scripts\activate`*
    
3.  **Install dependencies:** The `requirements.txt` file lists all necessary libraries.
    
    ```
    pip install -r requirements.txt
    ```
    
4.  **Run the scraper:**
    
    ```
    python web_scraper.py
    ```
    
5.  **Check the output:** Upon completion, a new file named `books.csv` will be created in this directory containing the scraped book titles and prices.
