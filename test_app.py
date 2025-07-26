from app import app

def test_hello():
    client = app.test_client()
    response = client.get('/hello')
    assert response.data == b'Hello from Jenkins CI/CD!'
