from flask import Blueprint, render_template, redirect, make_response

from app.dal.service import UserService

quest_pages = Blueprint(
    "quests", __name__, static_folder="../../static", template_folder="../../templates"
)

service = UserService()


@quest_pages.route("/")
def redirect_to_quests():
    from app.routes.validation.login_validation import verify_is_logged_in

    user_id = verify_is_logged_in()
    if user_id:
        return redirect("/quests/%s" % user_id)
        # return display_quests(user_id)
    return redirect("/login")


@quest_pages.route("/<string:user_id>")
def display_quests(user_id: str):
    user = service.get_by_id(user_id)
    return render_template(
        "index.html", page_content="components/all_quests.html", quests=user.quests
    )
