from flask import Flask, render_template
app = Flask(__name__)


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
    return render_template("register/register.html")

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

