from flask import Flask
from flask_login import LoginManager
import os
from typing import Optional

from auth.user import load_user, User
from web.routes import routes


app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']


app.register_blueprint(routes)


login_manager = LoginManager(app)


@login_manager.user_loader
def _load_user(user_id: str) -> Optional[User]:
    return load_user(user_id)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    flask_env = os.environ.get('FLASK_ENV', '')
    if flask_env == 'dev':
        app.run(host='0.0.0.0', port=port, debug=True)
    else:
        app.run(host='0.0.0.0', port=port)
