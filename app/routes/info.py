from flask import Blueprint, flash, render_template, request

info_pages = Blueprint(
    "info", __name__, static_folder="../../static", template_folder="../../templates"
)


@info_pages.route("/contact", methods=["GET", "POST"])
def contact_form():
    message = ""
    if request.method == "POST":
        # send message
        message = (
            "Thank you for your message, we will get back to you as soon as possible."
        )
        flash(message)
    return render_template("contact_us.html")


@info_pages.route("/privacy-policy")
def privacy_policy():
    return render_template(
        "info_page.html", page_content="components/privacy_policy.html"
    )


@info_pages.route("/terms-of-service")
def terms_of_use():
    return render_template(
        "info_page.html", page_content="components/terms_of_service.html"
    )
