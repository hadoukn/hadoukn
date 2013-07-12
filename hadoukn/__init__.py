from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy

from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension

from hadoukn.security import (
    HadouknAuthenticationPolicy,
    groupfinder
)
from hadoukn.resources import Site
from hadoukn.request import (
    get_db,
    get_user
)
from hadoukn.models import initialize_base

# Models must all be imported before main() is run
from hadoukn.models.app import App
from hadoukn.models.collaborator import Collaborator
from hadoukn.models.logplex import Logplex
from hadoukn.models.release import Release
from hadoukn.models.user import User
from hadoukn.models.key import Key


def main(global_config, **settings):
    authentication_policy = HadouknAuthenticationPolicy(callback=groupfinder)
    authorization_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings,
                          root_factory=Site,
                          authentication_policy=authentication_policy,
                          authorization_policy=authorization_policy)

    # Sqlalchemy Configuration
    engine = engine_from_config(settings, prefix='sqlalchemy.')
    initialize_base(engine)
    config.registry.dbmaker = sessionmaker(bind=engine, extension=ZopeTransactionExtension())

    # Transaction manager
    config.include('pyramid_tm')

    # Security
    config.set_default_permission('authenticated')

    # Request
    config.add_request_method(get_db, name='db', property=True, reify=True)
    config.add_request_method(get_user, name='user', property=True, reify=True)

    # Routes
    config.add_route('index', '/')
    config.add_route('login', '/login')

    # Apps
    config.add_route('apps', '/apps')

    # User
    config.add_route('users', '/users')

    # Keys
    config.add_route('keys', '/keys')

    # Internal
    config.add_route('internal_git_command', '/internal/{app_name}/gitaction')

    config.scan('hadoukn.api')

    return config.make_wsgi_app()
