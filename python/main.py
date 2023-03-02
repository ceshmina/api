from flask import Flask
from google.cloud import firestore
import os


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world!'


@app.route('/diary')
def diary():
    fs_client = firestore.Client()
    entries = fs_client.collection('contents').document('diary') \
        .collection('months').document('202301') \
        .collection('entries').order_by('date', direction='DESCENDING').stream()

    return [entry.to_dict() for entry in entries]


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    flask_env = os.environ.get('FLASK_ENV', '')
    if flask_env == 'dev':
        app.run(host='0.0.0.0', port=port, debug=True)
    else:
        app.run(host='0.0.0.0', port=port)
