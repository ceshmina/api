from flask_login import UserMixin
from google.cloud import firestore
from typing import Optional


class User(UserMixin):
    def __init__(self, user_id: str):
        self.id = user_id


def get_user(user_id: str, password: str) -> Optional[User]:
    fs_client = firestore.Client()
    users = fs_client.collection('users').where('user_id', '==', user_id).stream()

    for user in users:
        if user_id == user.get('user_id') and password == user.get('password'):
            return User(user_id)
    
    return None


def load_user(user_id: str) -> User:
    return User(user_id)
