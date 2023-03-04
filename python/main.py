from flask import Flask
import os

from web.routes import routes


app = Flask(__name__)
app.register_blueprint(routes)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    flask_env = os.environ.get('FLASK_ENV', '')
    if flask_env == 'dev':
        app.run(host='0.0.0.0', port=port, debug=True)
    else:
        app.run(host='0.0.0.0', port=port)
