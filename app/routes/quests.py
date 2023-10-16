import json
from typing import List

from flask import Blueprint, render_template, redirect, make_response, request
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
