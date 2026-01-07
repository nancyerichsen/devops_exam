def test_public_route_accessible(client):
    """Test that the public route is accessible."""
    response = client.get('/public/')
    assert response.status_code == 200
    assert b"Public Page" in response.data

def test_index_route_accessible(client):
    """Test that the public route is accessible."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data
    assert b"This is a minimal web app developed with <a href=\"http://flask.pocoo.org/\">Flask</a> " in response.data
    assert b'<form action="/login" method="post" class="navbar-form navbar-right">' in response.data

def test_not_found_route(client):
    """Test that the 404 route is accessible."""
    response = client.get('/nonexistent/')
    assert response.status_code == 404
    assert b"Not Found (404)" in response.data

def test_wrong_method(client):
    """Test that the wrong method route is accessible."""
    response = client.post('/public/')
    assert response.status_code == 405
    assert b"method of your request is not" in response.data