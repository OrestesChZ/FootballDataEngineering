from asyncio import timeout
from http.client import responses

import requests


def get_wikipedia_page(url):
    import requests

    print("Getting wikipedia page...", url)

    try:
        response = requests.url(url, timeout=10)
        response.raise_for_status() # CHECK IF REQUEST SUCCESFUL

        return response.text
    except requests.RequestException as e:
        print(f"An error occured: {e}")

########

def get_wikipedia_data(html):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all("table", {"class" : "wikitable sortable"})[0]

    table_rows = table.find_all('tr')
    return table_rows