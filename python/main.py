from flask import Flask
import os


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world!'


if __name__ == '__main__':
    port = int(os.environ['PORT'])
    app.run(host='0.0.0.0', port=port)
