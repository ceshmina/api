from datetime import date
from google.cloud import firestore
from typing import Any


def lives() -> list[dict[str, Any]]:
    fs_client = firestore.Client()
    today = date.today().strftime('%Y-%m-%d')

    lives = fs_client.collection('contents').document('events') \
        .collection('lives').where('date', '>=', today).order_by('date').stream()

    return [live.to_dict() for live in lives]
