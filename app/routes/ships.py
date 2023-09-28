import uuid

from flask import Blueprint, redirect, render_template, request

from app.dal.service import ShipService
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
    return render_template(
        "create.html", content="components/ship_create.html", user_id=user_id
    )


@ship_pages.route("/edit/<int:ship_id>/<string:user_id>", methods=[GET, POST])
def edit_ship(ship_id: int, user_id: str):
    if not verify_is_logged_in():
        return redirect("/login")
    ship_service = ShipService()
    ship = ship_service.get_by_id(ship_id)
    if request.method == POST:
        pass

    return render_template(
        "edit.html", content="components/ship_edit.html", user_id=user_id, ship=ship
    )


@ship_pages.route("/delete/<int:ship_id>/<string:user_id>")
def delete_ship(ship_id: int, user_id: str):
    return redirect("/user")
