from pyramid.view import forbidden_view_config

from . import (
    api_exception_decorator_factory,
    BadRequest
)


@forbidden_view_config(renderer='json',
                       decorator=(api_exception_decorator_factory))
def login_redirect_api(request):
    raise BadRequest('failure', "You need to be logged in for that!")
