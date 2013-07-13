from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension


def get_db(request):
    maker = request.registry.dbmaker
    session = maker()

    def cleanup(request):
        session.close()
    request.add_finished_callback(cleanup)

    return session


def includeme(config):
    settings = config.registry.settings

    engine = engine_from_config(settings, prefix='sqlalchemy.')

    config.registry.dbmaker = sessionmaker(
        bind=engine,
        extension=ZopeTransactionExtension(),
    )
    config.add_request_method(get_db, name='db', reify=True)

    # pull in all of the models before initializing
    #config.scan('.')
    from .app import App
    from .daemon import Daemon
    from .dyno import Dyno
    from .logplex import Logplex
    from .release import Release
    from .user import User

    # FIXME: try to create missing tables here, should really be done in
    # a separate script
    from .meta import Base
    Base.metadata.create_all(engine)
