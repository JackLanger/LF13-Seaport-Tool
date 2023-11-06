import json

from flask import Blueprint, render_template, redirect, request, session, jsonify

from algorithm.capacityAlgorithm import CapacityAlgorithm
from algorithm.questProcessor import QuestProcessor
from algorithm.timeAlgorithm import TimeAlgorithm
from app.dal.dal import Dal
from app.models.quest import Quest
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

    selected_ships = request.form.getlist("selectedShips")

    session['selected_ship_names'] = selected_ships
    print(selected_ships)

    quest_dto = next((q for q in user.quests if q.id == id), None)

    quest = Quest()
    quest.update_from_dto(quest_dto)

    ships = [ship for ship in user.ships if selected_ships and ship.name in selected_ships]

    if request.method == 'POST':
        algorithm_type = request.form.get('algorithmType')

        if algorithm_type == AlgorithmType.TIME_CRITICAL.value:
            algorithm = TimeAlgorithm(ships, quest)
        elif algorithm_type == AlgorithmType.CAPACITY_CRITICAL.value:
            algorithm = CapacityAlgorithm(ships, quest)
        else:
            return jsonify({'error': 'Unsupported algorithm type'}), 400

        selected_ships = request.args.getlist("selectedShipIds")
        print(selected_ships)

        quest_processor = QuestProcessor(algorithm, ships, quest)
        result = quest_processor.process_quest()
        session['algorithm_result'] = Dal.serialize(result)

        ships_result = []
        resources_result = []

        for solution in result:
            ships_solution = []
            resources_solution = []
            for round_ in solution.getSolution():
                ships_round = [ship for ship, _ in round_.getRound()]
                resources_round = [resource for _, resource in round_.getRound()]
                print(resources_round)
                ships_solution.append(ships_round)
                resources_solution.append(resources_round)
            ships_result.append(ships_solution)
            resources_result.append(resources_solution)

        return render_template(
            "index.html",
            page_content="components/display_ships.html",
            quest=quest_dto,
            ships=user.ships,
            selected_ship_names=selected_ships,
            algorithm_result=result,
            ships_result=ships_result,
            resources_result=resources_result
        )

    return render_template(
        "index.html",
        page_content="components/compute_quest.html",
        quest=quest_dto,
        ships=user.ships,
        selected_ship_names=selected_ships
    )
