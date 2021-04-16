from pyramid.security import Allow, Authenticated


class AuthFactory(object):
    def __init__(self, request):
        self.__acl__ = [
            (Allow, Authenticated, 'view'),
        ]


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('media', 'media', cache_max_age=3600)
    config.add_route('home', '/', factory=AuthFactory)
