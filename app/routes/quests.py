from flask import Blueprint

quest_pages = Blueprint(
    "quests", __name__, static_folder="../../static", template_folder="../../templates"
)
