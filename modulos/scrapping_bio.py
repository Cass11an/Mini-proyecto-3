from bs4 import BeautifulSoup as bs
import requests

def get_biography(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...",
        "Accept-Language": "es-ES,es;q=0.9",
    }

    response = requests.get(url, headers= headers)

    soup = bs(response.text, 'html.parser')

    pageAll = soup.find('div',{'class': "mw-content-ltr mw-parser-output"})
    biography = pageAll.find('p').text

    header = soup.find('header', {'class': "mw-body-header vector-page-titlebar no-font-mode-scale"})
    title = header.find('h1').text

    bioDriver = {
        'title': title,
        'biography': biography
    }

    return bioDriver

