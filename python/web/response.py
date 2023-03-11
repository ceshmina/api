from typing import Any, Callable, Dict, Tuple


def build_response(route: Callable, **kwargs) -> Tuple[Dict[str, Any], int]:
    try:
        data = route(**kwargs)
        body = {'data': data}
        status = 200
    except Exception as message:
        body = {'message': str(message)}
        status = 500
    
    response = {'status': status, 'body': body}
    return response, status
