from server import app, flight
from flask import request, jsonify, abort, make_response, render_template

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/api/v1/quotes', methods=['GET', 'POST'])
def get_all_quotes():
    if request.method == 'GET':
        '''return the information of all the quotes'''
        return jsonify(flight.get_data_from_db_by_tablename('quotes'))
    if request.method == 'POST':
        '''modify/update the minimum price for <quote_id>'''
        print(request)
        if not request.args:
            print('POST request format needs to be /api/v1/quotes?quote_id=<quote_id>&min_price=<new_minimum_price>')
            abort(400)
        if not 'min_price' in request.args or 'quote_id' not in request.args :
            print('Missing one or more parameters')
            abort(400)
        quote_id = request.args['quote_id']
        new_price = request.args['min_price']
        print(quote_id)
        print(new_price)
        flight.update_min_price_by_quote_id(quote_id, new_price)
        return jsonify(flight.get_data_from_db_by_tablename('quotes'))
    else:
        return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/v1/quotes/<quote_id>', methods=['GET'])
def quote_id(quote_id):
    '''return the information for <quote_id>'''
    return render_template('quote.html', title = 'Cheapest flight from ORD to RGA', quote = flight.get_quote_by_id_from_db(quote_id))
    # return jsonify(flight.get_quote_by_id_from_db(quote_id))

@app.route('/api/v1/carriers', methods=['GET'])
def get_all_carriers():
    '''return the information for all carriers'''
    return jsonify(flight.get_data_from_db_by_tablename('carriers'))

@app.route('/api/v1/places', methods=['GET'])
def get_all_places():
    '''return the information for all places'''
    return jsonify(flight.get_data_from_db_by_tablename('places'))

@app.route('/api/v1/summary', methods=['GET'])
def get_quote_summary():
    '''return the summary of the quotes'''
    return render_template('summary.html', title = 'Summary - Cheapest flight from ORD to RGA', summary = flight.get_summary_from_db())
    # return jsonify(flight.get_summary_from_db())

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
