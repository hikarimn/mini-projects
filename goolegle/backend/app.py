#__init__.py
import time
import os
from flask import request


from flask import Flask 
from page_scroller import Page_scroller


app = Flask(__name__)
scroller = Page_scroller('https://google.com', 2, 100)
# flight.create_tables_and_fill_with_data()  # comment this line out when testing

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/api/v1/links', methods=['POST'])
def get_all_quotes():
    print(request.json)
    url = request.json['url']
    index = request.json['index']
    res = 'url = ' + url + ', index =  ' + index
    # print(scroller.run_script())
    # return request.json
    return res