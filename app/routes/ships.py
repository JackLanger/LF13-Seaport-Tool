import uuid

from flask import Blueprint, redirect, render_template, request, jsonify

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
    return ShipDTO(
        -1, ship_name, int(ship_capacity), int(ship_sailors), int(ship_level)
    )


def update_user(user, ship: ShipDTO):
    user.ships.append(ship)
    user_service.save(user)


@ship_pages.route("/create", methods=[POST])
def create_ship():
    user = verify_is_logged_in()
    user = user_service.get_by_id(user)
    if not user:
        return redirect("/login")

    ship = create_ship_dto(request.form)
    update_user(user, ship)

    return ship.json


def update_ship(ship_id: int, data: dict):
    ship = ship_service.get_by_id(ship_id)
    if name in data:
        ship.name = data[name]
    ship.capacity = int(data[capacity].replace('"', ""))
    ship.sailors = int(data[sailors].replace('"', ""))
    ship.level = int(data[level].replace('"', ""))
    success_state, ship, err = ship_service.save(ship)
    return jsonify(
        success=success_state,
        data=ship.json if ship else None,
        error=err.json if err else None,
    )


@ship_pages.route("/edit/<int:ship_id>", methods=[POST])
def edit_ship(ship_id: int):  # todo: this is not being called for id 1
    if not verify_is_logged_in():
        return redirect("/login")

    ship_data = request.form
    return update_ship(ship_id, ship_data)


@ship_pages.route("/delete/<int:ship_id>", methods=["POST"])
def delete_ship(ship_id: int):
    user = verify_is_logged_in()
    if not user:
        return redirect("/login")

    user = user_service.get_by_id(user)
    ships = list(filter(lambda s: s.id != ship_id, user.ships))
    if len(ships) == len(user.ships):
        return jsonify(success=False, error="Ship not found")

    user.ships = ships
    user_service.save(user)

    return jsonify(success=True)
