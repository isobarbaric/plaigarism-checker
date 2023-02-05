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
    results = []
    for div in search_results.find_all(recursive=False):
        text_location = div.select('div[class*="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"]')
        # print(text_location)
        if len(text_location) != 0:
            results.append(text_location[0].text)
    return results

# search_query = 'dog'
# with open('page.txt') as f:
#    response = f.read().strip()
# soup = BeautifulSoup(response, 'lxml')
# search_results = soup.find('div', class_='v7W49e')


search_results = google_search('dog')
print(search_results)

