from flask import Blueprint, redirect, url_for, flash, render_template, request
from app.routes.constants import GET, POST
from app.routes.validation.login_validation import verify_is_logged_in

ship_pages = Blueprint(
    "ships", __name__, static_folder="../../static", template_folder="../../templates"
)


@ship_pages.route("/create/<string:user_id>", methods=[GET, POST])
def create_ship(user_id):
    if not verify_is_logged_in():
        return redirect("/login")

    if request.method == POST:
        pass
    return render_template("create.html", content="components/ship_create.html")


@ship_pages.route("/edit/<int:ship_id>/<string:user_id>", methods=[GET, POST])
def create_ship(ship_id, user_id):
    if not verify_is_logged_in():
        return redirect("/login")

    if request.method == POST:
        pass
    return render_template("edit.html", content="components/ship_edit.html")
