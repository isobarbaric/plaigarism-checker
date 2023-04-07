import cfscrape
from bs4 import BeautifulSoup
from urllib.parse import quote
from trafilatura import fetch_url, extract
import time

class PlagarismChecker:

    def __init__(self):
        pass

    def validation(self, topic: str, text: str) -> dict:
        # can possibly try to fnd a way to extract topic from text itself
        relevant_links = PlagarismChecker.google_search(topic)

        # return {percentage details}
        return dict()

    @staticmethod
    def google_search(search_query: str, num_pages: int = 5) -> list[str]:

        # creating a search query string from exact search text
        modified_query = quote(search_query)

        scraper = cfscrape.create_scraper()
        base_url = f"https://www.google.com/search?q={modified_query}&start="

        results = []

        for i in range(num_pages):

            # getting a response and parsing it
            response = scraper.get(base_url + str(10*i)).text
            soup = BeautifulSoup(response, 'lxml')

            # finding div where search results are listed
            search_results = soup.find('div', class_='v7W49e')

            # looping through nested elements inside the div
            for div in search_results.find_all(recursive=False):

                # determining html element containing the link for a search result
                link_location = div.find(class_="yuRUbf")

                if link_location is not None:
                    link = link_location.a['href']
                    results.append(link.replace(' › ', '/'))

        return results

    @staticmethod
    def extract_content(links: list[str]) -> list[str]:
        extracted_text = []

        # looping through list containing links to webpages
        for url in links:

            # fetching page content at url
            downloaded = fetch_url(url)

            # extracting text and converting it to text
            result = extract(downloaded, favor_precision=True)
            extracted_text.append(result)

        return extracted_text

    @staticmethod
    def compute():
        pass

if "__name__" == "__main__":
    start = time.time()
    search_results = PlagarismChecker.google_search('dog', num_pages=2)
    text = PlagarismChecker.extract_content(search_results)
    print(text[1][:1000])
    print(time.time() - start)