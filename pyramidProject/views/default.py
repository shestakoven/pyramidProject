from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import models


@view_config(
    route_name='home',
    permission='view',
    renderer='pyramidProject:templates/home.jinja2',
)
def captures_view(request):
    """View all captures from db for authenticated users."""
    try:
        query = request.dbsession.query(models.Capture)
        captures = query.all()
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'captures': captures, 'project': 'pyramidProject'}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.md for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
