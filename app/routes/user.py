from flask import Blueprint, redirect, url_for, flash, render_template, request


from app.dal.service import UserService

user_pages = Blueprint(
    "user", __name__, static_folder="../../static", template_folder="../../templates"
)

GET = "GET"
POST = "POST"


@user_pages.route("/profiles")
def profiles():
    return "select your profile"


@user_pages.route("/profiles/create", methods=[GET, POST])
def save_profile():
    if request.method == POST:
        result = request.form
        return render_template("login.html", result=result)
    else:
        user = {"name": "jack", "age": 37}
        return render_template("login.html", user=user)


@user_pages.route("/")
def user_view():
    user = {"name": "jack", "age": 37}
    return render_template("user.html", user=user)


@user_pages.route("/user/register")
def register_user():
    if request.method == POST:
        username = request.form["user"]  # Your form's
        password = request.form["pass"]
        passwordConfirm = request.form["passConfirm"]
        user_service = UserService()
        error = None
        if not username:
            error = "User name is required"
        elif not password or not passwordConfirm:
            error = "Password is required"
        elif password != passwordConfirm:
            error = "Password does not match confirmation"

        if error is None:
            try:
                user_service.register_new_user(username, password)
            except user_service.InvalidUserDetailsError:
                error = f"User {username} is already registered"
            else:
                return redirect(url_for("/user/login"))

        flash(error)

    return render_template("register.html")
