from pyramid.config import Configurator
from pyramid_fullauth.events import AfterRegister

from .subscribers import commit_db


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
        config.add_subscriber(commit_db, AfterRegister)
        config.scan()
    return config.make_wsgi_app()
