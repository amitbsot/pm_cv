from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

def scrape_imdb(url):
    # Your scraping logic here (as previously provided)

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
