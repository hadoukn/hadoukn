from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Transaction manager
    config.include('pyramid_tm')

    config.include('.models')
    config.include('.security')
    config.include('.routes')

    # User
    config.add_route('users', '/users')
    config.add_route('user_by_key', '/users/key')

    # Keys
    config.add_route('keys', '/keys')

    # Internal
    config.add_route('internal_git_command', '/internal/{app_name}/gitaction')

    config.scan('.api')
    return config.make_wsgi_app()
