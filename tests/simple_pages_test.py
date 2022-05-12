"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="dropdown-item" href="/git">Git</a>' in response.data
    assert b'<a class="dropdown-item" href="/docker">Docker</a>' in response.data
    assert b'<a class="dropdown-item" href="flask">Python/ Flask</a>' in response.data
    assert b'<a class="dropdown-item" href="cicd">CI/ CD</a>' in response.data
    assert b'<a class="dropdown-item" href="/pylint">Pylint' in response.data
    assert b'<a class="dropdown-item" href="/aaa">AAA Testing</a>' in response.data
    assert b'<a class="dropdown-item" href="/oops">OOPs</a>' in response.data
    assert b'<a class="dropdown-item" href="/solid">SOLID</a>' in response.data


def test_request_home(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Web Development" in response.data


def test_pylint_page(client):
    """This makes the pylint page"""
    response = client.get("/pylint")
    assert response.status_code == 200
    assert b"Object" in response.data


def test_aaa_page(client):
    """This makes the AAA page"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b"Testing" in response.data


def test_oops_page(client):
    """This makes the OOPs page"""
    response = client.get("/oops")
    assert response.status_code == 200
    assert b"Object" in response.data


def test_solid_page(client):
    """This makes the SOLID page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"SOLID" in response.data


def test_git_page(client):
    """This makes the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data


def test_docker_page(client):
    """This makes the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data


def test_flask_page(client):
    """This makes the flask page"""
    response = client.get("/flask")
    assert response.status_code == 200
    assert b"Python" in response.data


def test_about_page(client):
    """This makes the ci/cd page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"intern" in response.data


def test_register_page(client):
    """This makes the ci/cd page"""
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Register" in response.data


def test_login_page(client):
    """This makes the ci/cd page"""
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data