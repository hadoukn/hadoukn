from pyramid.security import unauthenticated_userid
from hadoukn.models.user import User


def get_db(request):
    maker = request.registry.dbmaker
    session = maker()

    def cleanup(request):
        session.close()
    request.add_finished_callback(cleanup)

    return session


def get_user(request):
    db = request.db
    api_key = unauthenticated_userid(request)
    if api_key is not None:
        # this should return None if the user doesn't exist
        # in the database
        return User.by_api_key(db, api_key)
    return None
