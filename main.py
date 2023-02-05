import cfscrape
from bs4 import BeautifulSoup
from urllib.parse import quote
from trafilatura import fetch_url, extract
import time

class PlaigarismChecker:
    def __init__(self):
        pass

    def check(topic: str, text: str) -> dict:
        # can possibly try to fnd a way to extract topic from text itself
        relevant_links = PlaigarismChecker.google_search(topic)

        # return {percentage details}
        pass

    @staticmethod
    def __google_search(search_query: str, num_pages: int = 5) -> list[str]:
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

    @staticmethod
    def __extract_content(links: list[str]) -> list[str]:
        extracted_text = []
        for url in links:
            downloaded = fetch_url(url)
            result = extract(downloaded, favor_precision=True)
            extracted_text.append(result)
        return extracted_text

    @staticmethod
    def compute():
        pass

start = time.time()
search_results = google_search('dog', num_pages=2)
text = extract_content(search_results)
print(text[1][:1000])
print(time.time() - start)


