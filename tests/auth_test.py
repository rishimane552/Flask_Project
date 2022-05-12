"""This test the homepage"""
from app.db.models import User

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_auth_pages(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200


def test_index_page_logged_in(client):
    """This tests for user login functionality"""
    with client:
        client.post('/login', data=dict(email='test@gmail.com', password='test'))
        res = client.get('/')
        assert res.status_code == 200


def test_user_registration(client):
    """ This ensures user can register"""
    with client:
        response = client.post('register/', data=dict(email='test2@gmail.com',
                                                      password='test', confirm='test'
                                                      ), follow_redirects=True)
        res = client.get('/login')
        assert res.status_code == 200


def test_logged_in_user_dashboard_access(client, application):
    """ This ensures logged_in user can access dashboard"""
    with application.app_context():
        email = 'test@test.com'
        password = 'test1234'
        response = client.post("/register", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)
        response = client.post("/login", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)
        response = client.get("/dashboard")
        assert response.status_code == 302




def test_denying_dashbaord(client, application):
    """This test to check while entering wrong username/ Password"""
    with application.app_context():
        email = 'test@test.com'
        password = 'test1234'
        wrong_email = 'abc@abc.com'
        wrong_password = 'testtest'
        user = User.query.filter_by(email=email).first()
        assert user is None
        response = client.post("/register", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)
        user = User.query.filter_by(email=email).first()
        assert user is None
        response = client.post("/login", data=dict(email=wrong_email, password=wrong_password, confirm=password),
                               follow_redirects=True)
        user = User.query.filter_by(email=wrong_email).first()
        assert user is None
        response = client.get("/dashboard")
        assert response.status_code is not 200