from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('pyramid_tm')
        config.include('.routes')
        config.include('.models')
        config.include('pyramid_basemodel')
        config.include('pyramid_fullauth')
        config.scan()
    return config.make_wsgi_app()
