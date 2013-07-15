from pyramid.view import view_config
from hadoukn.api import api_exception_decorator_factory


@view_config(route_name='internal_git_command',
             request_method='POST',
             renderer='json',
             decorator=(api_exception_decorator_factory))
def git_command(request):
    return {}
