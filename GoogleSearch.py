# this is a simple program that simplifies the search on google
# Here is a simple algorithm of how the program works

# • Gets search keywords from the command line arguments.
# •	 Retrieves the search results page.
# •	 Opens a browser tab for each result.


# This means our code will need to do the following:
# •	 Read the command line arguments from sys.argv.
# •	 Fetch the search result page with the requests module.
# •	 Find the links to each search result.
# •	 Call the webbrowser.open() function to open the web browser

import requests, sys, webbrowser, bs4
print('Googling')

# Downloading the web page
requestDownload = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

# checking for the status of the request
checkStatus = requestDownload.raise_for_status()
print(checkStatus)

# retriving common searches

#the line below creates the BeautifulSoup object that downloads that obtains the text from the html page
soup = bs4.BeautifulSoup(requestDownload.text)

# Open a browser tab for each 

# the downloaded page then uses the selector 
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))












