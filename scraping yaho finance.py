import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://finance.yahoo.com/quote/AAPL/'

# Send a GET request to the website
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the stock price on the page
price = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).get_text()

print(f'AAPL Stock Price: {price}')
