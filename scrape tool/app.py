from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        url = request.get_json()['url']
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad requests
        return jsonify(response.text)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
