import uuid

from flask import Blueprint, redirect, render_template, request

from app.dal.service import ShipService, UserService
from app.models.ship import ShipDTO
from app.routes.constants import GET, POST
from app.routes.validation.login_validation import verify_is_logged_in
from app.routes.constants import name, capacity, level, sailors

ship_pages = Blueprint(
    "ships", __name__, static_folder="../../static", template_folder="../../templates"
)

user_service = UserService()
ship_service = ShipService()


def create_ship_dto(form):
    ship_name = form["name"]
    ship_capacity = form["capacity"]
    ship_sailors = form["sailors"]
    ship_level = form["level"]
    return ShipDTO(-1, name, int(ship_capacity), int(ship_sailors), int(ship_level))


def save_ship_dto(ship: ShipDTO):
    return ship_service.create_new(ship)


def update_user(user, ship: ShipDTO):
    user.ships += ship
    user_service.save(user)


@ship_pages.route("/create", methods=[GET, POST])
def create_ship():
    user = verify_is_logged_in()
    user = user_service.get_by_id(user)
    if not user:
        return redirect("/login")

    if request.method == POST:
        ship = save_ship_dto(create_ship_dto(request.form))
        update_user(user, ship)

    return render_template("create.html", content="components/ship_create.html")


@ship_pages.route("/edit/<int:ship_id>", methods=[GET, POST])
def edit_ship(ship_id: int):    # todo: this is not being called for id 1
    if not verify_is_logged_in():
        return redirect("/login")
    ship = ship_service.get_by_id(ship_id)
    if request.method == POST:
        ship.name = request.form[name]
        ship.capacity = request.form[capacity]
        ship.sailors = request.form[sailors]
        ship.level = request.form[level]
        ship_service.save(ship)

        return redirect("/user")

    return render_template(
        "edit.html", content="components/ship_edit.html", ship=ship
    )


@ship_pages.route("/level-up/<int:ship_id>")
def level_up(ship_id):
    user = verify_is_logged_in()
    user = user_service.get_by_id(user)
    if user:
        ship = ship_service.get_by_id(ship_id)
        ship.level += 1
        ship_service.save(ship)
        return redirect("/user")
    return redirect("/login")


@ship_pages.route("/delete/<int:ship_id>")
def delete_ship(ship_id: int):
    user = verify_is_logged_in()
    user = user_service.get_by_id(user)
    if user:
        user.ships[:] = (s for s in user.ships if s.id != ship_id)
        ship_service.delete(ship_id)
        user_service.save(user)

    return redirect("/user")
