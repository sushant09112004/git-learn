# File: scrape.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the website to scrape
url = 'https://example.com'  # Replace with the actual URL you want to scrape

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Scraping all headings (h1 tags)
    headings = soup.find_all('h1')
    
    # Extract the text from each heading and store it in a list
    heading_list = [heading.text.strip() for heading in headings]
    
    # Convert the list of headings to a DataFrame
    df = pd.DataFrame(heading_list, columns=['Headings'])
    
    # Save the data to a CSV file inside the 'output' folder
    df.to_csv('output/scraped_data.csv', index=False)
    
    print("Scraping completed successfully! Data saved to 'output/scraped_data.csv'.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
