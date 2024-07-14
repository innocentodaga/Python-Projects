from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
options = Options()
options.add_argument('--headless')  # Run in headless mode (without a UI)
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# Path to the chromedriver executable
service = Service('path/to/chromedriver')

# Set up the Chrome driver
driver = webdriver.Chrome(service=service, options=options)

# Open the target website
driver.get('https://www.example.com')

# Find elements and extract data
elements = driver.find_elements(By.CLASS_NAME, 'example-class')
for element in elements:
    print(element.text)

# Close the browser
driver.quit()
