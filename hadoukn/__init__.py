from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Transaction manager
    config.include('pyramid_tm')

    config.include('.models')
    config.include('.security')
    config.include('.routes')

    config.scan('.api')

    return config.make_wsgi_app()
