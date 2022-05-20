
import sys
import requests
from bs4 import BeautifulSoup


def search_wiki(path, queries):
    url = f"https://en.wikipedia.org{path}"
    try:
        res = requests.get(url=url)
        res.raise_for_status()
    except requests.HTTPError as e:
        if res.status_code == 404:
            return print("It's a dead end !")
        return print(e)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.find(id='firstHeading').text
    if title in queries:
        return print("It leads to an infinite loop !")
    print(title)
    queries.append(title)
    if title == 'Philosophy':
        return print(f"{len(queries)} roads from {queries[0]} to Philosophy")
    content = soup.find(id='mw-content-text')
    links = content.select('p > a')
    for link in links:
        # print("+", link.get('href')[link.get('href').rfind("/")+1:], "+")
        if link.get('href') is not None and link['href'].startswith('/wiki/'):
            return search_wiki(link['href'], queries)
    return print("It leads to a dead end !.")


def get_road_to_philosophy(searched_str):
    queries_list = []
    search_wiki('/wiki/'+searched_str, queries_list)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_road_to_philosophy(sys.argv[1])
    else:
        print("Wrong Input! Type exactly one argument")
