from colander import (
    SchemaNode,
    Mapping,
    Integer,
    String
)
from pyramid.view import view_config
from hadoukn.api import (
    api_exception_decorator_factory
)
from hadoukn.models.user import User
from hadoukn.models.key import Key


@view_config(route_name='users',
             request_method='GET',
             renderer='json',
             decorator=(api_exception_decorator_factory))
def users(request):
    db = request.db

    # Schema
    schema = SchemaNode(Mapping(),
                        SchemaNode(Integer(), name='id'))
    payload = schema.deserialize(request.json)

    users = User.by_params(db, **payload)
    return users


@view_config(route_name='user_by_key',
             request_method='GET',
             renderer='json',
             decorator=(api_exception_decorator_factory))
def user_by_key(request):
    db = request.db

    # Schema
    schema = SchemaNode(Mapping(),
                        SchemaNode(String(), name='key_key'))
    payload = schema.deserialize(request.json)

    key = Key.by_key_key(db, payload['key_key'])
    if key:
        return key.user
