from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)
CORS(app)

# Rate limiting setup
REQUESTS_PER_MINUTE = 10
ALLOWED_IPS = set()

def is_allowed_ip(ip):
    return ip in ALLOWED_IPS

def add_ip(ip):
    ALLOWED_IPS.add(ip)

def remove_expired_ips():
    current_time = time.time()
    expired_ips = {ip for ip, timestamp in ALLOWED_IPS if timestamp < current_time - 60}
    ALLOWED_IPS.difference_update(expired_ips)

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        ip = request.remote_addr
        if not is_allowed_ip(ip):
            return jsonify({'error': 'Rate limit exceeded. Try again later.'}), 429

        url = request.get_json()['url']
        data = scrape_imdb(url)
        add_ip(ip)  # Add IP to allowed list
        remove_expired_ips()  # Clean up expired IPs from the allowed list
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def scrape_imdb(url):
    # Your scraping logic here
    # ...

if __name__ == '__main__':
    app.run(debug=True)
