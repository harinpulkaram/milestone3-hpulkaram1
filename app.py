import random
import os


from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user

from app import db
from models import User, Rating
from get_data import Getmovie

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return "Failed to Login"


@app.route("/")
def pageSetup():
    getCast = ", ".join(Getmovie.Getcast)
    return render_template(
        "pageSetup.html",
        getTitle=Getmovie.Gettitle,
        getPoster=Getmovie.Getposter,
        getTagline=Getmovie.Gettagline,
        getOverview=Getmovie.Getoverview,
        getCast=getCast,
        getRatings=Getmovie.Getratings,
        getBoxOffice=Getmovie.Getrevenue,
    )


@app.route("/login", methods=["GET", "POST"])
def login(username):
    if len(list(User)):
        for m in User:
            if username == m[username]:
                getResponse = "Logged In"
                return Flask.render_template("pageSetup.html", getResponse=getResponse)

            else:
                getResponse = "User does not exist, please register"
                return Flask.render_template("login.html", getResponse=getResponse)


@app.route("/register", methods=["GET", "POST"])
def register(username):
    if len(list(User)):
        for m in User:
            if username == m[username]:
                getResponse = "User already exists"
                return Flask.render_template("login.html", getResponse=getResponse)
            else:
                getResponse = "User added, please log in"
                addUsername = User(username=username)
                db.session.add(addUsername)
                db.session.commit()
                return Flask.render_template("login.html")


app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8080)),
)
