from validation.login_validation import (
    verify_is_logged_in,
    create_cookies,
    passw,
    user,
)

from flask import Flask, render_template, request, flash, make_response, redirect
from routes.constants import GET, POST
from routes.user import user_pages
from routes.quests import quest_pages
from routes.ships import ship_pages

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.register_blueprint(user_pages, url_prefix="/user")
app.register_blueprint(quest_pages, url_prefix="/quests")
app.register_blueprint(ship_pages, url_prefix="/ships")


@app.route("/index")
def dashboard():
    if verify_is_logged_in():
        return redirect("/login", code=302)
    return render_template("index.html")


@app.route("/")
def home():
    if verify_is_logged_in():
        return redirect("/login", code=302)
    return redirect("/index")


@app.route("/login", methods=[GET, POST])
def login():
    if request.method == POST:
        error = "The credentials provided did not match."
        form_data = request.form
        if not form_data[user]:
            error = "You have to supply a username in order to login."
        from dal.service import UserService

        service = UserService()
        username = form_data[user]
        if service.verify_credentials(username, form_data[passw]):
            resp = make_response(render_template("index.html"))
            create_cookies(resp, username)
            return resp

        flash(error)
    return render_template("login.html")


@app.route("/register", methods=[GET, POST])
def register_user():
    if request.method == POST:
        from dal.service import UserService

        password = request.form[passw]
        username = request.form[user]
        email = request.form["email"]
        error = ""
        service = UserService()

        if not password or not username or not email:
            error = "You have to fill in all fields in order to create an account."
        elif service.register_new_user(username, password, email):
            resp = make_response(render_template("index.html"))
            create_cookies(resp, username)
            return resp

        flash(error)

    return render_template("register.html")


if __name__ == "__main__":
    app.run()
