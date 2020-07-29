#__init__.py
import time
import os
from flask import request, Flask, jsonify 

from page_scroller import Page_scroller

app = Flask(__name__)

@app.route('/api/v1/links', methods=['POST'])
def get_all_quotes():
    url = request.json['url']
    index = request.json['index']
    scroller = Page_scroller(url, 5, index)
    scraped_urls = scroller.run_scraper()
    result = {
        'original_url': url,
        'list_size': len(scraped_urls),
        'index': int(index),
        'urls': scraped_urls
    }
    return jsonify(result)