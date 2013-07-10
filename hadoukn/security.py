USERS = {'jayd3e': 'default'}


def groupfinder(userid, request):
    if userid in USERS:
        return []
