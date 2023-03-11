from typing import Any, Callable, NamedTuple


class Response(NamedTuple):
    response: dict[str, Any]
    status: int


def build_response(route: Callable, **kwargs: Any) -> Response:
    try:
        data = route(**kwargs)
        body = {'data': data}
        status = 200
    except Exception as message:
        body = {'message': str(message)}
        status = 500

    response = {'status': status, 'body': body}
    return Response(response=response, status=status)
