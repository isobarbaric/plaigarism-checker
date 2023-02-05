import cfscrape
from bs4 import BeautifulSoup
from urllib.parse import quote

def google_search(search_query: str, num_pages: int = 5) -> list[str]:
    modified_query = quote(search_query)
    scraper = cfscrape.create_scraper()
    base_url = f"https://www.google.com/search?q={modified_query}&start="
    results = []
    for i in range(num_pages):
        print(base_url + str(10*i))
        response = scraper.get(base_url + str(10*i)).text
        soup = BeautifulSoup(response, 'lxml')
        search_results = soup.find('div', class_='v7W49e')
        for div in search_results.find_all(recursive=False):
            link_location = div.find(class_="yuRUbf")
            if link_location is not None:
                link = link_location.a['href']
                results.append(link.replace(' › ', '/'))
    return results

search_results = google_search('dog')
for link in search_results:
    print(link)

