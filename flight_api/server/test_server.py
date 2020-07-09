import json
import pytest
import requests

from server import app
url = 'http://127.0.0.1:5000' 

@pytest.fixture
def app():
    yield app

def test_index(app):
    res = requests.get(url+'/') 
    assert res.status_code == 200

def test_quote_id(app):
    res = requests.get(url + '/api/v1/quotes/1')
    assert res.status_code == 200

def test_quotes(app):
    res = requests.get(url + '/api/v1/quotes')
    data = res.json()
    assert res.status_code == 200
    assert len(data) > 0

def test_get_all_carriers(app):
    res = requests.get(url + '/api/v1/carriers')
    print(type(res))
    assert res.status_code == 200
    assert len(res.json()) > 0

def test_get_all_places(app):
    res = requests.get(url + '/api/v1/places')
    print(type(res))
    data = res.json()
    assert len(data) != 0
    assert res.status_code == 200

def test_get_quote_summary(app):
    res = requests.get(url + '/api/v1/summary')
    print(type(res))
    assert res.status_code == 200
    assert 'avg_min_price' in res.json()