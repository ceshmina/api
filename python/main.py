from flask import Flask
import os


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world!'


@app.route('/diary')
def diary():
    return 'まだ日記はありません'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    flask_env = os.environ.get('FLASK_ENV', '')
    if flask_env == 'dev':
        app.run(host='0.0.0.0', port=port, debug=True)
    else:
        app.run(host='0.0.0.0', port=port)
