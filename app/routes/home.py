from flask import (
    render_template,
    request,
    flash,
    make_response,
    redirect,
    Blueprint,
)

from app.routes.constants import GET, POST
from app.routes.validation.login_validation import (
    verify_is_logged_in,
    create_cookies,
    passw,
    user,
    register_cookie,
    expire_existing_cookies,
)

home_pages = Blueprint(
    "home", __name__, static_folder="../../static", template_folder="../../templates"
)


@home_pages.route("/logout")
def logout():
    resp = make_response(redirect("/login"))
    expire_existing_cookies(resp)
    return resp


@home_pages.route("/index")
def dashboard():
    if not verify_is_logged_in():
        return redirect("/login", code=302)
    user_id = request.cookies.get(register_cookie)
    return redirect("/user/" + user_id)


@home_pages.route("/")
def home():
    if not verify_is_logged_in():
        return redirect("/login", code=302)
    return redirect("/index")


@home_pages.route("/login", methods=[GET, POST])
def login():
    if request.method == POST:
        error = "The credentials provided did not match."
        form_data = request.form
        if not form_data[user]:
            error = "You have to supply a username in order to login."
        from app.dal.service import UserService

        service = UserService()
        username = form_data[user]
        if service.verify_credentials(username, form_data[passw]):
            resp = make_response(render_template("index.html"))
            create_cookies(resp, username)
            return resp

        flash(error)
    return render_template("login.html")


@home_pages.route("/register", methods=[GET, POST])
def register_user():
    if request.method == POST:
        from app.dal.service import UserService

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
