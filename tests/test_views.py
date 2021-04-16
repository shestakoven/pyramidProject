from pyramidProject import models
from pyramidProject.views.default import captures_view
from pyramidProject.views.notfound import notfound_view


def test_my_view_success(app_request, dbsession):
    model = models.Capture(path='test_path', camera='abc')
    dbsession.add(model)
    dbsession.flush()

    info = captures_view(app_request)
    assert app_request.response.status_int == 200
    assert info['captures'][0].path == 'test_path'
    assert info['project'] == 'pyramidProject'


def test_notfound_view(app_request):
    info = notfound_view(app_request)
    assert app_request.response.status_int == 404
    assert info == {}
