from colander import Invalid
from pyramid.response import Response


class BadRequest(Exception):
    _dict = None

    def __init__(self, status, msg):
        self.status = status
        self.msg = msg


def api_exception_decorator_factory(view):
    def api_exception_decorator(context, request):
        try:
            return view(context, request)
        except Invalid as e:
            payload = {
                'status': 'failure',
                'msg': e.asdict()
            }
        except BadRequest as e:
            payload = {
                'status': e.status,
                'msg': e.msg
            }
        return Response(status='400 Bad Request',
                        content_type='application/json',
                        json=payload)
    return api_exception_decorator
