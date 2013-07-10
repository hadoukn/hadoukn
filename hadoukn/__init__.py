from pyramid.config import Configurator
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

from hadoukn.security import groupfinder
from hadoukn.resources import Site
from hadoukn.request import get_db


def main(global_config, **settings):
    authentication_policy = SessionAuthenticationPolicy(callback=groupfinder)
    authorization_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings,
                          root_factory=Site,
                          authentication_policy=authentication_policy,
                          authorization_policy=authorization_policy)

    # Sqlalchemy Configuration
    engine = engine_from_config(settings, prefix='sqlalchemy.')
    config.registry.dbmaker = sessionmaker(bind=engine)
    config.add_request_method(get_db, name='db', property=True, reify=True)

    # Sessions
    config.include('pyramid_redis_sessions')

    # Views
    config.add_static_view('static', 'hadoukn:static')

    # Routes
    config.add_route('index', '/')

    config.scan('hadoukn.views')

    return config.make_wsgi_app()
