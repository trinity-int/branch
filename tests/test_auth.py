
import pytest
from flask import g, session
from flaskr.db import get_db


def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'email': 'a', 'password': 'a', 'firstName': 'a', 'lastName': 'a', 'age': '18', 'gender': 'a'}
    )
    assert 'http://localhost/auth/login' == response.headers['Location']

    with app.app_context():
        assert get_db().execute(
            "select * from Users where email = 'a'",
        ).fetchone() is not None


# @pytest.mark.parametrize(('email', 'password', 'firstName', 'lastName', 'age', 'gender', 'message'), (
#     ('', '', '', '', '', '', b'email is required.'),
#     ('a', '', '', '', '', '', b'Password is required.'),
#     ('a', 'a', '', '', '', '', b'First Name is required.'),
#     ('a', 'a', 'a', '', '', '', b'Last Name is required.'),
#     ('a', 'a', 'a', 'a', '', '', b'Age is required.'),
#     ('a', 'a', 'a', 'a', 'a', '', b'Gender is required.'),
#     ('test', 'test', 'test', 'test', 'test', 'test', b'already registered'),
# ))
# def test_register_validate_input(client, email, password, firstName, lastName, age, gender, message):
#     response = client.post(
#        '/auth/register',
#         data={'email': email, 'password': password, 'firstName': firstName, 'lastName': lastName, 'age': age, 'gender': gender}
#     )
#     assert message in response.data

# def test_login(client, auth):
#     assert client.get('/auth/login').status_code == 200
#     response = auth.login()
#     assert response.headers['Location'] == 'http://localhost/'

#     with client:
#         client.get('/')
#         assert session['user_id'] == 1
#         assert g.user['username'] == 'test'


# @pytest.mark.parametrize(('username', 'password', 'message'), (
#     ('a', 'test', b'Incorrect username.'),
#     ('test', 'a', b'Incorrect password.'),
# ))
# def test_login_validate_input(auth, username, password, message):
#     response = auth.login(username, password)
#     assert message in response.data

# def test_logout(client, auth):
#     auth.login()

#     with client:
#         auth.logout()
#         assert 'user_id' not in session