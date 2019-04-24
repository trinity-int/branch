import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        age = request.form['age']
        gender = request.form['gender']
        db = get_db()
        error = None

        if not email:
            error = 'Email is required'
        elif not password:
            error = 'Password is required'
        elif db.execute(
            'select ID from Users where Email = ?', (email,)
        ).fetchone() is not None:
            error = 'User {} is already registered'.format(email)

        if error is None:
            # There's probably a better way to format this query
            db.execute(
                'insert into Users (FirstName, LastName, Email, Password, Age, Gender) values (?, ?, ?, ?, ?, ?)',
                (firstName, lastName, email, generate_password_hash(password), age, gender)
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('register/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'select * from Users where Email = ?', (email,)
        ).fetchone()

        if email is None:
            error = 'Incorrect email'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            # this is stupid but it works
            return redirect('/events')

        flash(error)

    return render_template('login/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'select * from Users where ID = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('renderLanding'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)

    return wrapped_view

