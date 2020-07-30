#__init__.py
import time
import os
from flask import request, Flask, jsonify 
from page_crawler import Page_crawler

app = Flask(__name__)

@app.route('/api/v1/links', methods=['POST'])
def get_all_links():
    url = request.json['url']
    index = request.json['index']
    crawler = Page_crawler(url, 5, index)
    scraped_urls = crawler.run_crawler()
    result = {
        'original_url': url,
        'list_size': len(scraped_urls),
        'urls': scraped_urls
    }
    return jsonify(result)