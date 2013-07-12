import datetime

from colander import (
    SchemaNode,
    Mapping,
    String
)
from pyramid.view import view_config

from ..models.app import App
from ..models.collaborator import Collaborator
from . import api_exception_decorator_factory


@view_config(route_name='apps',
             request_method='POST',
             renderer='json',
             decorator=(api_exception_decorator_factory))
def apps_create(request):
    db = request.db
    settings = request.registry.settings

    schema = SchemaNode(Mapping(),
                        SchemaNode(String(), name='name'),
                        SchemaNode(String(), name='stack'))
    payload = schema.deserialize(request.json)

    app = App(created=datetime.datetime.now(),
              name=payload['name'],
              stack=payload['stack'],
              web_url='http://%s.%s' % (payload['name'], settings['hadoukn.base_domain']),
              git_url='git@%s:%s.git' % (settings['hadoukn.base_domain'], payload['name']),
              user=request.user)

    Collaborator(user=request.user,
                 app=app)

    db.add(app)
    db.flush()
    return app
