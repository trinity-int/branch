
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

def test_login(client):
    assert client.get('/auth/login').status_code == 200

    client.post(
        '/auth/register', data={'email': 'a', 'password': 'a', 'firstName': 'a', 'lastName': 'a', 'age': '18', 'gender': 'a'}
    )

    response = client.post(
        '/auth/login', data={'email': 'a', 'password': 'a'}
    )
    assert 'http://localhost/events' == response.headers['Location']

def test_logout(client):
    response = client.get('/auth/logout')
    assert 'http://localhost/' == response.headers['Location']
