def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1> Welcome to the flask </h1>' in response.data

def test_user_route(client):
    response = client.get('/shrikant')
    assert response.status_code == 200
    assert b'<h1>welcome shrikant!</h1>' in response.data

def test_user_name_route(client):
    response = client.get('/user/shrikant')
    assert response.status_code == 200
    assert 'text/html' in response.content_type
    html = response.data.decode('utf-8')
    assert "<title>Hello</title>" in html

def test_macro_route(client):
    response = client.get('/user/form')
    print()
    assert response.status_code == 200

    # Check content-type for HTML
    assert 'text/html' in response.content_type

    # Check HTML content
    html = response.data.decode('utf-8')  # Decode the response content (bytes to string)
    assert "<title>Forms</title>" in html


