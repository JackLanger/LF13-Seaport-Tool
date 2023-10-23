import json
from typing import List

from flask import Blueprint, render_template, redirect, make_response, request, session, jsonify

from algorithm.capacityAlgorithm import CapacityAlgorithm
from algorithm.questProcessor import QuestProcessor
from algorithm.timeAlgorithm import TimeAlgorithm
from app.routes.validation.login_validation import verify_is_logged_in
from app.dal.service import UserService
from app.routes.constants import GET, POST
from app.enums.algorithm_type_enum import AlgorithmType

quest_pages = Blueprint(
    "quests", __name__, static_folder="../../static", template_folder="../../templates"
)

service = UserService()


@quest_pages.route("/")
def redirect_to_quests():
    user_id = verify_is_logged_in()
    if user_id:
        return display_quests(user_id)
    return redirect("/login")


def display_quests(user_id: str):
    user = service.get_by_id(user_id)
    return render_template(
        "index.html", page_content="components/all_quests.html", user=user
    )


@quest_pages.route("/delete/<int:id>", methods=[GET])
def delete_quest(id):
    user = verify_is_logged_in()
    if not user:
        return redirect("/login")
    user = service.get_by_id(user)
    quest = list(filter(lambda q: q.id == id, user.quests))[0]
    user.quests.remove(quest)
    service.save(user)
    return redirect("/")


@quest_pages.route("/info/<int:id>", methods=[GET])
def info_page(id):
    user = verify_is_logged_in()
    if not user:
        return redirect("/login")

    user = service.get_by_id(user)
    ships = user.ships
    quest = list(filter(lambda q: q.id == id, user.quests))[0]
    return render_template(
        "index.html",
        page_content="components/quest_info.html",
        quest=quest,
        ships=ships,
    )


@quest_pages.route("/create", methods=[POST, GET])
def create_quest():
    uid = verify_is_logged_in()
    if uid:
        user = service.get_by_id(uid)
        if request.method == "POST":
            from app.models.quest import QuestDTO, Resource

            resource_json = request.form["resources"]
            resource_data = json.loads(resource_json)
            resources = []
            for res in resource_data:
                amount = int(res["amount"])
                name = res["name"]
                resources.append(Resource(name, amount=amount))
            quest = QuestDTO(request.form["name"], resources=resources)
            user.quests.append(quest)
            service.save(user)
            return redirect("/quests")

        else:
            return render_template(
                "index.html", page_content="components/create_quest.html", user=user
            )
    return redirect("/login")


@quest_pages.route("/edit/<int:quest_id>/", methods=[POST, GET])
def edit_quest(quest_id: str):
    user = verify_is_logged_in()
    if not user:
        return redirect("/login")
    else:
        user = service.get_by_id(quest_id)
        quest = list(filter(lambda q: q.id == quest_id, user.quests))[0]

        if not quest:
            return redirect("/quests/create")
        else:
            return render_template(
                "index.html",
                page_content="components/edit_quest.html",
                user=user,
                quest=quest,
            )


@quest_pages.route("/<int:id>/compute", methods=[GET, POST])
def compute_quest(id):
    user = verify_is_logged_in()
    if not user:
        return redirect("/login")
    user = service.get_by_id(user)

    default_ship_names = ['Ship1', 'Ship2', 'Ship3']  # Replace with your default ship names

    selected_ship_names = session.get('selected_ship_names', default_ship_names)
    print(len(selected_ship_names))

    quest = next((q for q in user.quests if q.id == id), None)

    if request.method == 'POST':
        selected_ship_names = request.json.get('selectedShipNames', default_ship_names)
        session['selected_ship_names'] = selected_ship_names
        print(len(selected_ship_names))
        algorithm_type = request.json.get('algorithmType')
        ships = [ship for ship in user.ships if ship.name in selected_ship_names]

        if algorithm_type == AlgorithmType.TIME_CRITICAL.value:
            algorithm = TimeAlgorithm(ships, quest)
        elif algorithm_type == AlgorithmType.CAPACITY_CRITICAL.value:
            algorithm = CapacityAlgorithm(ships, quest)
        else:
            return jsonify({'error': 'Unsupported algorithm type'}), 400

        quest_processor = QuestProcessor(algorithm, ships, quest)
        result = quest_processor.process_quest()
        session['algorithm_result'] = result

        return render_template(
            "index.html",
            page_content="components/display_ships.html",
            quest=quest,
            ships=user.ships,
            selected_ship_names=selected_ship_names,
            algorithm_result=result
        )

    return render_template(
        "index.html",
        page_content="components/compute_quest.html",
        quest=quest,
        ships=user.ships,
        selected_ship_names=selected_ship_names
    )


@quest_pages.route("/<int:id>/display_ships", methods=[GET])
def display_ships(id):
    user = verify_is_logged_in()
    if not user:
        return redirect("/login")

    user = service.get_by_id(user)

    quest = next((q for q in user.quests if q.id == id), None)

    selected_ship_names = session.get('selected_ship_names', [])

    algorithm_result = session.get('algorithm_result', [])

    return render_template(
        "index.html",
        page_content="components/display_ships.html",
        quest=quest,
        ships=user.ships,
        selected_ship_names=selected_ship_names,
        algorithm_result=algorithm_result
    )
