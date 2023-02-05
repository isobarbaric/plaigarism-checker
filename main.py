import cfscrape
from bs4 import BeautifulSoup
from urllib.parse import quote

def google_search(search_query: str):
    modified_query = quote(search_query)
    url = f"https://www.google.com/search?q={modified_query}"
    scraper = cfscrape.create_scraper()
    response = scraper.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    search_results = soup.find('div', class_='v7W49e')
    for div in search_results.find('div', recursive=False):
        print(str(div) + '\n\n')
    results = []

search_query = 'dog'
with open('page.txt') as f:
    response = f.read().strip()
soup = BeautifulSoup(response, 'lxml')
search_results = soup.find('div', class_='v7W49e')
# print(str(search_results)[:500])
# assert len(search_results) == 1

for div in search_results.find_all(recursive=False):
    text_location = div.find('div', class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf')
    print(text_location.text)
    break

results = []

# google_search('dog')
