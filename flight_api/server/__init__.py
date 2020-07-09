#__init__.py
from flask import Flask 
from flight.Flight import Flight

app = Flask(__name__)
flight = Flight()
# flight.create_tables_and_fill_with_data()  # comment this line out when testing

from server import views