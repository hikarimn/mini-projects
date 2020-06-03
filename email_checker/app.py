import flask
from flask import request, jsonify, abort, make_response

app = flask.Flask(__name__)

emails = []

@app.route('/', methods=['GET'])
def home():
    return "<h1>Email Checker</h1><p>This site is a prototype API for an email checker.</p>"

@app.route('/api/v1/emails', methods=['GET'])
def get__all_emails():
    # get all the emails in the memory
    return jsonify(emails)

@app.route('/api/v1/emails/<int:email_id>', methods=['GET'])
def get_email(email_id):
    # get an email address based on id
    this_email = [email for email in emails if email['id'] == email_id]
    if len(this_email) == 0:
        abort(404)
    return jsonify({'email': this_email[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/v1/emails', methods=['POST'])
def create_email():
    # add new email adresses
    if not request.json:
        abort(400)
    if type(request.json) == list:
        new_emails = request.json
        for new_email in new_emails:
            if not 'email' in new_email:
                abort(400)
            email = {
                'id': get_max_index() + 1,
                'email': new_email['email']
            }
            emails.append(email)
        return jsonify(emails), 201
    if not 'email' in request.json:
        abort(400)
    if type(request.json['email']) == list:
        new_emails = request.json['email']
        for new_email in new_emails:
            email = {
                'id': get_max_index() + 1,
                'email': new_email
            }
            emails.append(email)
    else: 
        email = {
            'id': get_max_index() + 1,
            'email': request.json['email']
        }
        emails.append(email)
    return jsonify(emails), 201

def get_max_index():
    # help to find the unique id
    if len(emails) == 0:
        return len(emails)
    else:
        return emails[-1]['id']

@app.route('/api/v1/emails/<int:email_id>', methods=['PUT'])
def update_email(email_id):
    # update an email adress based on id
    email = [email for email in emails if email['id'] == email_id]
    if len(email) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'email' in request.json and type(request.json['email']) != str:
        abort(400)
    email[0]['email'] = request.json.get('email', email[0]['email'])
    return jsonify({'email': email[0]})

@app.route('/api/v1/emails/<int:email_id>', methods=['DELETE'])
def delete_email(email_id):
    # detele an email adress based on id
    email = [email for email in emails if email['id'] == email_id]
    if len(email) == 0:
        abort(404)
    emails.remove(email[0])
    return jsonify({'result': True})

@app.route('/api/v1/emails/unique', methods=['GET'])
def get_unique_emails():
    # get a number of unique email addresses
    unique_emails = set()
    for email in  emails:
        x = email['email'].split("@")
        y = x[0].split("+")
        z = y[0].replace(".", "")
        x = z + "@" + x[1]
        unique_emails.add(x)
    return jsonify({'result': str(len(unique_emails)), 'unique emails': list(unique_emails)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)