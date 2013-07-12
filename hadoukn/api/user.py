from colander import (
    SchemaNode,
    Mapping,
    String
)
from pyramid.view import view_config
from hadoukn.api import (
    api_exception_decorator_factory,
    BadRequest
)
from hadoukn.models.key import Key


@view_config(route_name='users',
             request_method='GET',
             renderer='json',
             decorator=(api_exception_decorator_factory))
def users(request):
    db = request.db

    schema = SchemaNode(Mapping(),
                        SchemaNode(String(), name='key_type'),
                        SchemaNode(String(), name='key_key'))
    payload = schema.deserialize(request.json)

    key = Key.by_key_key(db, payload['key_key'])
    if key:
        return key.user
    else:
        raise BadRequest('failure', "user with attached key doesn't exist")
