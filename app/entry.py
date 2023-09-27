from flask import Flask, render_template, request
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
    return render_template("index.html")


@app.route("/")
def home():
    from flask import redirect

    return redirect("signin", code=302)


@app.route("/signin", methods=[GET, POST])
def login():
    if request.method == POST:
        from flask import redirect

        # handle request
        return redirect("/index")

    return render_template("login.html")


@app.route("/signup", methods=[GET, POST])
def register_user():
    if request.method == POST:
        return render_template("register.html")
        # process post form data

    return render_template("register.html")


if __name__ == "__main__":
    app.run()
