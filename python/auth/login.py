from flask_login import current_user, login_user, logout_user

from auth.user import get_user


def login(user_id: str, password: str):
    user = get_user(user_id, password)
    if user is not None:
        login_user(user)
        return f'Logged in as {user_id}'
    else:
        return 'Wrong user ID or password'


def user():
    user_id = current_user.get_id()
    return f'Logged in as {user_id}'


def logout():
    logout_user()
    return 'Logged out'
