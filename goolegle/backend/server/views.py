from server import app, flight
from flask import request, jsonify, abort, make_response, render_template

@app.route('/time')
def get_current_time():
    return {'time': time.time()}