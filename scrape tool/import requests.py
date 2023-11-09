from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

def scrape_imdb(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.select_one('h1').get_text(strip=True)

        # Extracting data based on CSS selectors
        description = soup.select_one('div.summary_text').get_text(strip=True)
        episode = soup.find('div', class_='bp_heading').get_text(strip=True) if soup.find('div', class_='bp_heading') else '0'
        season = soup.find('div', class_='bp_heading').get_text(strip=True) if soup.find('div', class_='bp_heading') else '0'
        genre = soup.select('div.see-more.inline.canwrap h4:contains("Genres") + span a')
        genre = ', '.join([g.get_text(strip=True) for g in genre]) if genre else '0'
        rating = soup.select_one('span[itemprop="ratingValue"]').get_text(strip=True)
        cast = soup.select('div.credit_summary_item span[itemprop="name"]')
        cast = ', '.join([c.get_text(strip=True) for c in cast]) if cast else '0'
        release_date = soup.select_one('a[title="See more release dates"]').get_text(strip=True) if soup.select_one('a[title="See more release dates"]') else '0'
        origin = soup.select_one('div.txt-block:contains("Country:")').next_sibling.strip() if soup.select_one('div.txt-block:contains("Country:")') else '0'
        language = soup.select_one('div.txt-block:contains("Language:")').next_sibling.strip() if soup.select_one('div.txt-block:contains("Language:")') else '0'
        runtime = soup.select_one('time').get_text(strip=True) if soup.select_one('time') else '0'

        # Create a dictionary to store the scraped data
        data = {
            'title': title,
            'description': description,
            'episode': episode,
            'season': season,
            'genre': genre,
            'rating': rating,
            'cast': cast,
            'release_date': release_date,
            'origin': origin,
            'language': language,
            'runtime': runtime
        }

        # Replace empty strings with '0'
        for key, value in data.items():
            if not value:
                data[key] = '0'

        return data

    except Exception as e:
        return {'error': str(e)}

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        url = request.get_json()['url']
        data = scrape_imdb(url)
        return jsonify(data)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'An error occurred. Please check the URL and try again.'})

if __name__ == '__main__':
    app.run(debug=True)
