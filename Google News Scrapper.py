import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    
    def scrape(self):
        try:
            res = urllib.request.urlopen(self.site)
            html = res.read()
            parser = 'html.parser'
            sp = BeautifulSoup(html, parser)
            for tag in sp.find_all('a'):
                url = tag.get('href')
                if url is None:
                    continue
                if '/articles/' in url:
                    if not url.startswith('http'):
                        url = 'https://news.google.com' + url[1:]
                    print('\n' + url)
        except Exception as e:
            print(f'An error occurred: {e}')

# Creating an instance of the Scraper class
news_site = 'https://news.google.com/'

# Calling the scrape method
scraper = Scraper(news_site)
scraper.scrape()
