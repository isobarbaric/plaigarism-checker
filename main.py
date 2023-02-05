import cfscrape
from bs4 import BeautifulSoup
from urllib.parse import quote

def google_search(search_query: str):
    modified_query = quote(search_query)
    scraper = cfscrape.create_scraper()
    url = f"https://www.google.com/search?q={modified_query}&start=0"
    response = scraper.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    search_results = soup.find('div', class_='v7W49e')
    results = []
    for div in search_results.find_all(recursive=False):
        link_location = div.find_all(class_="yuRUbf")
        if len(link_location) != 0:
            try:
                link = link_location[0].a['href']
                results.append(link.replace(' › ', '/'))
            except:
                pass
    return results


# search_query = 'dog'
# with open('page.txt') as f:
#    response = f.read().strip()
# soup = BeautifulSoup(response, 'lxml')
# search_results = soup.find('div', class_='v7W49e')


search_results = google_search('dog')
print(search_results)

