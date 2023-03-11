from datetime import date
from google.cloud import firestore
from typing import Any, Dict, List


def diary(month: str) -> List[Dict[str, Any]]:
    try:
        query_date = date(int(month[:4]), int(month[4:6]), 1)
    except Exception:
        raise Exception('Invalid requested month: month must be specified as yyyymm')

    query_month = query_date.strftime('%Y%m')

    fs_client = firestore.Client()
    entries = fs_client.collection('contents').document('diary') \
        .collection('months').document(query_month) \
        .collection('entries').order_by('date', direction='DESCENDING').stream()

    return [entry.to_dict() for entry in entries]
