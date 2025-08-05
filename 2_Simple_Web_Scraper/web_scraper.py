# web_scraper.py
#
# A simple and robust web scraper designed to extract book titles and prices
# from http://books.toscrape.com, a website made for scraping practice.
#
# Author: PyraVim
# Version: 1.0.0
#
# This script demonstrates:
# - Making HTTP requests to a web server.
# - Parsing HTML content with BeautifulSoup.
# - Handling pagination to scrape multiple pages.
# - Storing extracted data into a CSV file using pandas.
# - Implementing cybersecurity and ethical scraping best practices.

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import logging

# --- Configuration ---

# The starting URL for the web scraping target.
# Using a dedicated practice site is crucial for a public portfolio.
BASE_URL = "http://books.toscrape.com/catalogue/"
CURRENT_URL = BASE_URL + "page-1.html"

# Security Best Practice: Set a realistic User-Agent.
# Many websites block requests from default Python user agents (like 'python-requests/2.x').
# A common browser User-Agent makes the request look like it's coming from a real user,
# reducing the risk of being blocked.
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Ethical Best Practice: Rate Limiting.
# A delay between requests prevents overwhelming the server with traffic,
# which can cause performance issues for the site and get your IP address banned.
# A 1-second delay is a reasonable starting point.
REQUEST_DELAY_SECONDS = 1

# --- Main Application Logic ---

def scrape_books():
    """
    Main function to orchestrate the web scraping process.
    It handles pagination, extracts book data, and saves it to a CSV.
    """
    print("--- Starting Web Scraper ---")
    
    # A list to hold the data for each book we find.
    all_books_data = []
    
    # Keep track of the current page number for user feedback.
    page_number = 1
    
    # The URL will be updated to point to the next page in each iteration.
    next_page_url = CURRENT_URL

    while next_page_url:
        print(f"\n[INFO] Scraping page {page_number}: {next_page_url}")

        try:
            # Make the HTTP GET request to the current page.
            # A timeout is set to prevent the script from hanging indefinitely on a non-responsive server.
            response = requests.get(next_page_url, headers=HEADERS, timeout=10)
            
            # This will raise an HTTPError if the HTTP request returned an unsuccessful status code (e.g., 404, 500).
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Network request failed: {e}")
            print("[INFO] Stopping scraper due to network issues.")
            break

        # Parse the HTML content of the page using BeautifulSoup.
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all book entries on the page. Each book is contained in an <article> tag with the class 'product_pod'.
        books_on_page = soup.find_all('article', class_='product_pod')

        if not books_on_page:
            print("[INFO] No books found on this page. This could be the end of the catalogue.")
            break

        # Loop through each book found on the page to extract its details.
        for book in books_on_page:
            try:
                # Extract the book title. The title is in an 'a' tag within the 'h3' tag.
                # We access the 'title' attribute for the full title.
                title = book.h3.a['title']
                
                # Extract the price. The price is in a <p> tag with the class 'price_color'.
                # We get the text and strip the '£' symbol.
                price_text = book.find('p', class_='price_color').text
                price = float(price_text.strip('£'))

                # Store the cleaned data in a dictionary.
                all_books_data.append({'title': title, 'price_in_pounds': price})

            except (AttributeError, KeyError, ValueError) as e:
                # Robustness: If a single book's HTML is malformed, log the error and continue
                # with the next book instead of crashing the entire script.
                print(f"[WARNING] Could not process a book entry. Error: {e}. Skipping.")

        # --- Pagination Logic ---
        
        # Find the 'next' button to see if there's another page.
        next_button = soup.find('li', class_='next')
        
        if next_button and next_button.a:
            # If a 'next' button with a link is found, construct the URL for the next page.
            next_page_relative_url = next_button.a['href']
            next_page_url = BASE_URL + next_page_relative_url
            page_number += 1
        else:
            # If no 'next' button is found, we've reached the last page.
            print("\n[INFO] Reached the last page of the catalogue.")
            next_page_url = None # This will cause the while loop to terminate.

        # Apply the ethical rate limit before making the next request.
        print(f"[INFO] Waiting for {REQUEST_DELAY_SECONDS} second(s) before next request...")
        time.sleep(REQUEST_DELAY_SECONDS)

    # --- Data Storage ---

    if not all_books_data:
        print("\n[INFO] No data was scraped. Exiting without creating a CSV file.")
        return

    print(f"\n[SUCCESS] Scraped a total of {len(all_books_data)} books.")
    print("[INFO] Converting data to pandas DataFrame and saving to CSV...")

    # Convert the list of dictionaries into a pandas DataFrame.
    # This structure is ideal for easy conversion to CSV and other formats.
    df = pd.DataFrame(all_books_data)
    
    # Save the DataFrame to a CSV file.
    # index=False prevents pandas from writing row indices into the file.
    try:
        df.to_csv('books.csv', index=False, encoding='utf-8')
        print("[SUCCESS] Data successfully saved to books.csv")
    except IOError as e:
        print(f"[ERROR] Could not write to CSV file: {e}")

    print("\n--- Web Scraper Finished ---")


# This standard Python construct ensures that the scrape_books() function is called
# only when the script is executed directly (e.g., `python web_scraper.py`).
if __name__ == "__main__":
    scrape_books()
