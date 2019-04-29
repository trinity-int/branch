from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

from datetime import datetime

bp = Blueprint('events', __name__)

@bp.route("/events")
@login_required
def renderEvents():
    db = get_db()
    events = db.execute('select * from Events order by EventDate').fetchall()
    return render_template('events/events.html', events=events)

@bp.route("/events/create", methods=('GET', 'POST'))
@login_required
def createEvent():
    if request.method == 'POST':
        eventName = request.form['eventName']
        eventDate = request.form['eventDate']
        eventTime = request.form['eventTime']
        description = request.form['description']
        maxCapacity = request.form['maxCapacity']
        host = g.user['id']
        dateCreated = datetime.today().strftime('%Y-%m-%d')
        eventLocation = request.form['eventLocation']
        eventAddress = request.form['eventAddress']
        eventType = request.form['eventType']
        eventDifficulty = request.form['eventDifficulty']
        db = get_db()
        error = None # TODO: error handling

        db.execute(
            'insert into Events (EventName, EventDate, EventTime, Description, MaxCapacity, Host, DateCreated, EventLocation, EventAddress, EventType, EventDifficulty) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (eventName, eventDate, eventTime, description, maxCapacity, host, dateCreated, eventLocation, eventAddress, eventType, eventDifficulty)
        )

        db.commit()
        return redirect(url_for('events.renderEvents'))

    return render_template('events/createEvents.html')

@bp.route("/events/register", methods=('GET', 'POST'))
@login_required
def registerForEvent():
    if request.method == 'POST':
        eventID = request.form['eventID']
        userID = request.form['userID']
        db = get_db()
        error = None

        if db.execute(
            'select * from UsersRegistered where EventID = (?) and UserID = (?)',
            (eventID, userID)
        ).fetchone() is not None:
            error = "User is already registered!"

        if error == None:
            db.execute(
                'insert into UsersRegistered (EventID, UserID) values (?, ?)',
                (eventID, userID)
            )

            db.commit()
            return redirect(url_for('events.renderEvents'))

        flash(error)

    return redirect(url_for('events.renderEvents'))
