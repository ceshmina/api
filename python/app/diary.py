from google.cloud import firestore
from typing import Any, Dict, List


def diary() -> List[Dict[str, Any]]:
    fs_client = firestore.Client()
    entries = fs_client.collection('contents').document('diary') \
        .collection('months').document('202301') \
        .collection('entries').order_by('date', direction='DESCENDING').stream()

    return [entry.to_dict() for entry in entries]
