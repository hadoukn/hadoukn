import datetime

from colander import (
    SchemaNode,
    Mapping,
    String
)
from pyramid.view import view_config

from ..models.app import App
from . import api_exception_decorator_factory


@view_config(route_name='apps',
             request_method='POST',
             renderer='json',
             decorator=(api_exception_decorator_factory))
def apps_create(request):
    db = request.db

    schema = SchemaNode(Mapping(),
                        SchemaNode(String(), name='name'))
    payload = schema.deserialize(request.json)

    app = App(created=datetime.datetime.now(),
              name=payload['name'],
              user=request.user)
    db.add(app)

    db.flush()
    return app
