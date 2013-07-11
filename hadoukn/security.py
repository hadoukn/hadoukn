from zope.interface import implementer
from pyramid.interfaces import IAuthenticationPolicy
from pyramid.authentication import CallbackAuthenticationPolicy

from hadoukn.models.user import User


def groupfinder(api_key, request):
    db = request.db

    user = db.query(User).filter_by(api_key=api_key).first()
    if user is not None:
        return []
    return None


@implementer(IAuthenticationPolicy)
class HadouknAuthenticationPolicy(CallbackAuthenticationPolicy):
    def __init__(self, callback=None):
        self.callback = callback

    def unauthenticated_userid(self, request):
        return request.GET.get('api_key')

    def remember(self, request, principal, **kw):
        return []

    def forget(self, request):
        return []
