import pytest
from flask import g, session
from flaskr.db import get_db

# Create dummy user and login
def login(client):
    client.post(
        '/auth/register', data={'email': 'a', 'password': 'a', 'firstName': 'a', 'lastName': 'a', 'age': '18', 'gender': 'a'}
    )

    client.post(
        '/auth/login', data={'email': 'a', 'password': 'a'}
    )

def createEvent(client):
    client.post(
        '/events/create', data={'eventName': 'my cool event', 'eventDate': '2019-10-10', 'eventTime': '12:00', 'description': 'test', 'maxCapacity': 5, 'Host': 1, 'DateCreated': '2019-10-10', 'eventLocation': 'home', 'eventAddress': '', 'eventType': 'test', 'eventDifficulty': 'Beginner'}
    )

# Testing event creation
def test_createEvent(client, app):
    login(client)

    assert client.get('/events/create').status_code == 200

    response = client.post(
        '/events/create', data={'eventName': 'event', 'eventDate': '2019-10-10', 'eventTime': '12:00', 'description': 'test', 'maxCapacity': 5, 'Host': 1, 'DateCreated': '2019-10-10', 'eventLocation': 'home', 'eventAddress': '', 'eventType': 'test', 'eventDifficulty': 'Beginner'}
    )

    assert 'http://localhost/events' == response.headers['Location']

    with app.app_context():
        assert get_db().execute(
            "select * from Events where eventName = 'event'",
        ).fetchone() is not None

def test_renderEvents(client):
    login(client)

    assert client.get('/events').status_code == 200

    createEvent(client)

    # Checking to see that the event name is on the page
    assert 'my cool event' in str(client.get('/events').data)

def test_registerForEvent(client, app):
    login(client)
    createEvent(client)

    response = client.post(
        '/events/register', data={'eventID': 1, 'userID': 1}
    )

    assert 'http://localhost/events' == response.headers['Location']

    with app.app_context():
        assert get_db().execute(
            "select * from UsersRegistered where EventID = 1 and UserID = 1",
        ).fetchone() is not None

def test_unregisterForEvent(client, app):
    login(client)
    createEvent(client)

    response = client.post(
        '/events/unregister', data={'eventID': 1, 'userID': 1}
    )

    assert 'http://localhost/events' == response.headers['Location']

    with app.app_context():
        assert get_db().execute(
            "select * from UsersRegistered where EventID = 1 and UserID = 1",
        ).fetchone() is None
