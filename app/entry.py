from flask import Flask, render_template

from routes.user import user_pages
from routes.quests import quest_pages
from routes.ships import ship_pages
from routes.info import info_pages
from routes.home import home_pages

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.register_blueprint(user_pages, url_prefix="/user")
app.register_blueprint(quest_pages, url_prefix="/quests")
app.register_blueprint(ship_pages, url_prefix="/ships")
app.register_blueprint(info_pages, url_prefix="/info")
app.register_blueprint(home_pages, url_prefix="/")


@app.errorhandler(404)
def resource_not_found(error):
    return render_template("error.html", error_details=error)


if __name__ == "__main__":
    app.run()
