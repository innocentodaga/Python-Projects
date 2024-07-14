import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.indeed.com/jobs?q=software+developer&l='

# Headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Upgrade-Insecure-Requests': '1'
}

# Send a GET request to the website with headers
response = requests.get(url, headers=headers)
response.raise_for_status()  # Check that the request was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all job titles on the page
jobs = soup.find_all('h2', class_='jobTitle')

# Loop through each job title and print it
for job in jobs:
    title = job.get_text(strip=True)
    print(title)
