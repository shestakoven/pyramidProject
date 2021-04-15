from pyramidProject import models

def test_redirect(testapp, dbsession):

    res = testapp.get('/', status=302)
    assert res.body

def test_notfound(testapp):
    res = testapp.get('/badurl', status=404)
    assert res.status_code == 404
