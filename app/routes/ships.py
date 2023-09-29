import uuid

from flask import Blueprint, redirect, render_template, request

from app.dal.service import ShipService
from app.models.ship import ShipDTO
from app.routes.constants import GET, POST
from app.routes.validation.login_validation import verify_is_logged_in
from app.routes.constants import name, capacity, level, sailors

ship_pages = Blueprint(
    "ships", __name__, static_folder="../../static", template_folder="../../templates"
)


def create_ship_dto(form):
    ship_name = form["name"]
    ship_capacity = form["capacity"]
    ship_sailors = form["sailors"]
    ship_level = form["level"]
    return ShipDTO(-1, name, int(ship_capacity), int(ship_sailors), int(ship_level))


def save_ship_dto(ship: ShipDTO):
    ship_service = ShipService()
    return ship_service.create_new(ship)


def update_user(user_id, ship: ShipDTO):
    from app.dal.service import UserService

    user_service = UserService()
    user_dto = user_service.get_by_id(user_id)
    user_dto.ships += ship
    user_service.update(user_dto)


@ship_pages.route("/create/<string:user_id>", methods=[GET, POST])
def create_ship(user_id):
    if not verify_is_logged_in():
        return redirect("/login")

    if request.method == POST:
        ship = save_ship_dto(create_ship_dto(request.form))
        update_user(user_id, ship)

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
        ship.name = request.form[name]
        ship.capacity = request.form[capacity]
        ship.sailors = request.form[sailors]
        ship.level = request.form[level]
        ship_service.update(ship)

        return redirect("/user/%s" % user_id)

    return render_template(
        "edit.html", content="components/ship_edit.html", user_id=user_id, ship=ship
    )


@ship_pages.route("/level-up/<int:ship_id>/<string:user_id>")
def level_up(ship_id, user_id):
    return redirect("/user/%s" % user_id)


@ship_pages.route("/delete/<int:ship_id>/<string:user_id>")
def delete_ship(ship_id: int, user_id: str):
    return redirect("/user")
