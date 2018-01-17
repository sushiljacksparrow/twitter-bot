import requests
from bs4 import BeautifulSoup as bs
import os

url = 'https://www.pexels.com/search/tech/'


page = requests.get(url)
soup = bs(page.text, 'html.parser')

images_tags = soup.findAll('img')

if not os.path.exists('tech'):
    os.makedirs('tech')

os.chdir('tech')

x = 0

for image_tag in images_tags:
    try:
        image_url = image_tag['src']
        source = requests.get(image_url)
        if source.status_code == 200:
            with open('tech-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(image_url).content)
                f.close()
                x = x + 1
    except:
        pass
                     
