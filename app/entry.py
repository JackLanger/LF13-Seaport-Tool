from datetime import timedelta

from flask import Flask, render_template, redirect, session, request

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


app.config[
    "SECRET_KEY"
] = "fa1e42f63b053a98d9f2f57976f84edf\
39b227596926a15d841c996af94d07ca\
f81ffca1cdde6f5e619c70c3d0a6b310\
193217cea1f55c7ff589e138f3982383\
29f08bd8aa6a857adee5d1c61d2d4031\
205162eef85eb4a24b109a96f839c9b6\
21c2559ed0102c1f9455ad2b0f8c3ee5\
b79a8b1e9dba173d822bc8c615ededc6\
2a918962a18f55abe66244621f3702cb\
353c84acf48d6329a600229188ff2b14"

app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=1)

# TODO(Jack): rework Cookie Sessions for login redirect, to expire on Browser close.
#
# @app.before_request
# def setup():
#     session.permanent = True
#
#
# @app.route("/")
# def login_redirect():
#     if check_login(session, False):
#         user_id = request.cookies.get("Seaport-User-Verified")
#         return redirect("/user/%s" % user_id)
#     return redirect("/login")
#
#
# def check_login(session, requires_elevated):
#     if "username" not in session:
#         return False
#     elif session["username"] == "admin":
#         return True
#     elif session["username"] == "regular" and not requires_elevated:
#         return True
#     return False


@app.errorhandler(404)
def resource_not_found(error):
    return render_template(
        "index.html", page_content="components/error.html", error_details=error
    )


if __name__ == "__main__":
    app.run()
