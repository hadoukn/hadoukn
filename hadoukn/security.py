from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import unauthenticated_userid
from pyramid.security import (
    Allow,
    Authenticated,
    Everyone,
)

from hadoukn.models.user import User


class HadouknAuthenticationPolicy(object):

    def unauthenticated_userid(self, request):
        return request.GET.get('api_key')

    def authenticated_userid(self, request):
        if request.user:
            return request.user.id

    def effective_principals(self, request):
        principals = [Everyone]
        user = request.user
        if user:
            principals += [Authenticated]
        return principals

    def remember(self, request, principal, **kw):
        return []

    def forget(self, request):
        return []


class Site(object):
    __acl__ = [(Allow, Authenticated, 'authenticated')]

    def __init__(self, request):
        pass


def get_user(request):
    db = request.db
    api_key = unauthenticated_userid(request)
    if api_key is not None:
        # this should return None if the user doesn't exist
        # in the database
        return User.by_api_key(db, api_key)


def includeme(config):
    authn_policy = HadouknAuthenticationPolicy()
    authz_policy = ACLAuthorizationPolicy()

    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.set_root_factory(Site)

    config.set_default_permission('authenticated')

    config.add_request_method(get_user, name='user', reify=True)
