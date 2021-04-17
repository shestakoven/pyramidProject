import threading

from pyramid.config import Configurator
from pyramid_fullauth.events import AfterRegister

from .helpers import make_captures
from .helpers import make_media_dir
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
    make_media_dir.main()
    thread = threading.Thread(target=make_captures.main)
    thread.start()
    return config.make_wsgi_app()
