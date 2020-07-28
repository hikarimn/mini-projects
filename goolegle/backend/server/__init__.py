#__init__.py
from flask import Flask 
from scroller.page_scroller import Page_scroller

app = Flask(__name__)
scroller = Page_scroller()
# flight.create_tables_and_fill_with_data()  # comment this line out when testing

from server import views