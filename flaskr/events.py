from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route("/events")
@login_required
def renderEvents():
    db = get_db()
    events = db.execute('select * from Events').fetchall()
    return render_template('events/events.html', events=events)

@bp.route("/events/create", methods=('GET', 'POST'))
@login_required
def createEvent():
    if request.method == 'POST':
        eventName = request.form['eventName']
        eventDate = request.form['eventDate']
        description = request.form['description']
        maxCapacity = request.form['maxCapacity']
        host = request.form['host']
        dateCreated = request.form['dateCreated']
        eventLocation = request.form['eventLocation']
        eventAddress = request.form['eventAddress']
        eventType = request.form['eventType']
        eventDifficulty = request.form['eventDifficulty']
        db = get_db()
        error = None # TODO: error handling

        db.execute(
            'insert into Events (EventName, EventDate, Description, MaxCapacity, Host, DateCreated, EventLocation, EventAddress, EventType, EventDifficulty values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (eventName, eventDate, description, maxCapacity, host, dateCreated, eventLocation, eventAddress, eventType, eventDifficulty)
        )

        db.commit()
        return redirect(url_for('renderEvents'))

    return render_template('events/createEvents.html')
