from flask import Flask, render_template

from routes.user import user_pages
from routes.quests import quest_pages
from routes.ships import ship_pages

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.register_blueprint(user_pages, url_prefix="/user")
app.register_blueprint(quest_pages, url_prefix="/quests")
app.register_blueprint(ship_pages, url_prefix="/ships")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
