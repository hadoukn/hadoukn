import datetime

from colander import (
    SchemaNode,
    Mapping,
    String
)
from pyramid.view import view_config

from hadoukn.api import api_exception_decorator_factory
from hadoukn.models.key import Key


@view_config(route_name='keys',
             request_method='POST',
             renderer='json',
             decorator=(api_exception_decorator_factory))
def keys_add(request):
    db = request.db

    schema = SchemaNode(Mapping(),
                        SchemaNode(String(), name='key_type'),
                        SchemaNode(String(), name='key_key'),
                        SchemaNode(String(), name='key_comment'))
    payload = schema.deserialize(request.json)

    key = Key.by_key_key(db, payload['key_key'])
    if not key:
        key = Key(created=datetime.datetime.now(),
                  key_type=payload['key_type'],
                  key_key=payload['key_key'],
                  key_comment=payload['key_comment'],
                  user=request.user)
        db.add(key)

    return key
