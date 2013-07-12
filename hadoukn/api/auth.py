import base64

from pyramid.view import view_config
from pyramid.security import NO_PERMISSION_REQUIRED

from ..models.user import User
from . import api_exception_decorator_factory


@view_config(route_name='login',
             request_method='GET',
             renderer='json',
             permission=NO_PERMISSION_REQUIRED,
             decorator=(api_exception_decorator_factory))
def login(request):
    db = request.db

    authorization = request.headers.get('Authorization')
    if authorization:
        authmeth, auth = authorization.split(' ', 1)

        if authmeth.lower() == 'basic':
            auth = base64.b64decode(auth.strip()).decode('ascii')
            username, password = auth.split(':', 1)

            # Get user
            user = User.by_username(db, username)
            if user and user.validate_password(password):
                return {
                    'username': user.username,
                    'api_key': user.api_key
                }

    return {
        'api_key': None
    }
