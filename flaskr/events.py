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
