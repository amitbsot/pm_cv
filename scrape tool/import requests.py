import requests
from bs4 import BeautifulSoup

def scrape_imdb(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = {}

    # These selectors might need to be updated depending on the exact structure of the IMDb page
    selectors = {
        "CAST": "div.credit_summary_item",
        "CATEGORY": "div.see-more.inline.canwrap",
        "DESCRIPTION": "div.summary_text",
        "DIRECTOR": "div.credit_summary_item a",
        "LANGUAGE": "div.txt-block",
        "RATING": "div.ratingValue strong span",
        "RELEASE_DATE": "div.txt-block",
        "RESOLUTION": "div.txt-block",
        "RUN_TIME": "div.txt-block time",
        "EPISODE": "div.bp_heading",
        "EPISODE_TITLE": "div.title_wrapper h1",
        "SEASON": "div.bp_heading",
        "SUBTITLE": "div.txt-block",
        "TITLE": "div.title_wrapper h1",
        "TYPE": "div.subtext a"
    }

    for key, selector in selectors.items():
        element = soup.select_one(selector)
        data[key] = element.get_text(strip=True) if element else "0"

    return data

url = "https://www.imdb.com/title/tt0111161/"  # replace with your IMDb link
data = scrape_imdb(url)
print(data)