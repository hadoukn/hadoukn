from colander import (
    SchemaNode,
    Mapping,
    Integer
)
from pyramid.view import view_config
from hadoukn.api import (
    api_exception_decorator_factory
)


@view_config(route_name='users',
             request_method='GET',
             renderer='json',
             decorator=(api_exception_decorator_factory))
def users(request):
    schema = SchemaNode(Mapping(),
                        SchemaNode(Integer(), name='id'))
    payload = schema.deserialize(request.json)
