import requests, os, bs4

# specify the url we are targeting
url = 'https://xkcd.com/'

# store the comics in a folder xkcd
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    print('Downloading page %s...' % url)
    
    # download the page
    request = requests.get(url)
    
    # check status
    try:
        request.raise_for_status()
    except Exception as exc:
        print(f'There was a problem: {exc}')
        break
    
    # retrieving the text from the page
    soup = bs4.BeautifulSoup(request.text, 'html.parser')

    # Find the URL of the comic image
    comicElement = soup.select('#comic img')
    if comicElement == []:
        print('Could not find comic image')
    else:
        comicUrl = comicElement[0].get('src')
        if not comicUrl.startswith('http'):
            comicUrl = 'http:' + comicUrl
        
        # Downloading the image
        print('Downloading image %s...' % (comicUrl))
        request = requests.get(comicUrl)
        try:
            request.raise_for_status()
        except Exception as exc:
            print(f'There was a problem downloading the image: {exc}')
            break
        
        # Save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in request.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the previous button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com/' + prevLink.get('href')
print('Done')
