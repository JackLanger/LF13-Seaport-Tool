from flask import Blueprint, redirect, url_for, flash, render_template, request


from app.dal.service import UserService

quest_pages = Blueprint(
    "quests", __name__, static_folder="../../static", template_folder="../../templates"
)
