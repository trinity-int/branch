import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from . import db
from flask import send_from_directory

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

    @app.route("/")
    def renderLanding():
        return render_template("landing.html")

    @app.route("/login")
    def renderLogin():
        return render_template("login/login.html")

    @app.route("/login/forgot")
    def renderForgotPassword():
        return render_template("login/forgot.html")

    @app.route("/register")
    def renderRegister():
        return render_template("register/register.html", cond='')

    @app.route("/profile")
    def renderProfile():
        return render_template("profile/profile.html")

    @app.route("/profile/myevents")
    def renderMyEvents():
        return render_template("profile/myevents.html")

    @app.route("/events")
    def renderEvents():
        return render_template("events/events.html")  

    @app.route("/settings")
    def renderSettings():
        return render_template("settings/settings.html")

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'), 
            'favicon.ico',mimetype='image/vnd.microsoft.icon')

    return app
