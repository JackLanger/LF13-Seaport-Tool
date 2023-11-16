import json

from flask import Blueprint, render_template, redirect, request, jsonify

from algorithm.capacityAlgorithm import CapacityAlgorithm
from algorithm.timeAlgorithm import TimeAlgorithm
from app.models.quest import Resource
from app.routes.validation.login_validation import verify_is_logged_in
from app.dal.service import UserService
from app.routes.constants import GET, POST

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


@quest_pages.route("/delete/<int:id>", methods=[POST])
def delete_quest(id):
    from flask import jsonify

    user = verify_is_logged_in()
    if not user:
        return redirect("/login")

    user = service.get_by_id(user)
    quest = list(filter(lambda q: q.id == id, user.quests))[0]

    if quest:
        user.quests.remove(quest)
        service.save(user)
        return jsonify(success=True)

    return jsonify(success=False, error="Quest not found")


@quest_pages.route("/create", methods=[POST])
def create_quest():
    uid = verify_is_logged_in()
    if uid:
        user = service.get_by_id(uid)

        from app.models.quest import QuestDTO, Resource

        resource_json = request.form["resources"]
        resource_data = json.loads(resource_json)
        resources = []
        for res in resource_data:
            amount = int(res["amount"])
            name = res["name"]
            resources.append(Resource(name, amount=amount))

        quest = QuestDTO(len(user.quests), request.form["name"], resources=resources)
        user.quests.append(quest)
        service.save(user)
        return jsonify(success=True, code=200, quest=quest.json)

    return redirect("/login")


@quest_pages.route("/edit/<int:quest_id>/", methods=[POST])
def edit_quest(quest_id: str):
    user = verify_is_logged_in()
    if not user:
        return redirect("/login")
    else:
        user = service.get_by_id(user)
        quest = list(filter(lambda q: q.id == quest_id, user.quests))[0]
        form = request.form
        quest.name = form["name"]
        quest.resources.clear()

        for res in json.loads(request.form["resources"]):
            quest.resources.append(Resource(res["name"], int(res["amount"])))

        service.save(user)
        resp = quest.json
        if not quest:
            return jsonify(success=False, code=500, error="Quest not found")
        else:
            return jsonify(success=True, code=200, quest=resp)


@quest_pages.route("/compute/<int:quest_id>", methods=[POST])
def compute_quest(quest_id):
    user = verify_is_logged_in()
    if not user:
        return redirect("/login")
    user = service.get_by_id(user)
    data = request.get_json()
    quest = list(filter(lambda q: q.id == quest_id, user.quests))[0]
    algo = None
    match data["algo"].lower():
        case "time":
            algo = TimeAlgorithm(user.ships, quest)
        case "capacity":
            algo = CapacityAlgorithm(user.ships, quest)
        case _:
            return jsonify(success=False, code=500, error="Unknown algorithm")
    result = algo.calculate()
    json_resp = jsonify(success=True, code=200, result=[r.to_json() for r in result])
    return json_resp
