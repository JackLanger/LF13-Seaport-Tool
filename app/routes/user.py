from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    make_response,
)

from app.dal.service import UserService
from app.routes.validation.login_validation import verify_is_logged_in

user_pages = Blueprint(
    "user", __name__, static_folder="../../static", template_folder="../../templates"
)

GET = "GET"
POST = "POST"


@user_pages.route("/")
def home():
    user_id = verify_is_logged_in()
    if user_id:
        resp = make_response(redirect("/user/%s" % user_id))
        return resp
    redirect("/login")


@user_pages.route("/<string:user_id>")
def user_view(user_id):
    # Create a UserDTO instance (you can replace this with your data retrieval logic)
    service = UserService()
    user = service.get_by_id(user_id)
    return render_template("user.html", user=user)
