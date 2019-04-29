import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask import send_from_directory

from . import db
from . import auth
from . import events

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    Bootstrap(app)

    # registering routes for registering/logging in
    app.register_blueprint(auth.bp)

    # registering routes for events
    app.register_blueprint(events.bp)
    app.add_url_rule('/', endpoint='renderLanding')

    @app.route("/")
    def renderLanding():
        return render_template("landing.html")

    @app.route("/login")
    def renderLogin():
        return render_template("login/login.html")

    @app.route("/login/forgot")
    def renderForgotPassword():
        return render_template("login/forgot.html")

    @app.route("/profile/myevents")
    @auth.login_required
    def renderMyEvents():
        return render_template("profile/myevents.html")

    @app.route("/settings")
    @auth.login_required
    def renderSettings():
        return render_template("settings/settings.html")

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'), 
            'favicon.ico',mimetype='image/vnd.microsoft.icon')

    # Defined here so the function(s) can be called from the templates
    @app.context_processor
    def utility_processor():
        def getUsersRegistered(eventID):
            d = db.get_db()
            userCount = d.execute(
                'select count(UserID) from UsersRegistered where EventID = (?)',
                (eventID,)
            ).fetchone()
            return userCount[0]

        def isUserRegistered(eventID, userID):
            d = db.get_db()
            users = d.execute(
                'select UserID from UsersRegistered where EventID = (?)',
                (eventID,)
            ).fetchall()

            for user in users:
                if user[0] == userID:
                    return True

            return False

        return dict(
            getUsersRegistered=getUsersRegistered,
            isUserRegistered=isUserRegistered
        )

    return app
