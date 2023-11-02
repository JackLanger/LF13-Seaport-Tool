from __future__ import annotations

import uuid

user_uid = "Seaport-User-Verified"

passw = "password"
user = "username"


def verify_is_logged_in() -> str | None:
    from flask import request

    username = request.cookies.get(user)
    user_uid_cookie = request.cookies.get(user_uid)
    if not username or not user_uid:
        return None
    return user_uid_cookie


def expire_existing_cookies(resp):
    resp.set_cookie(user, "", expires=0)
    resp.set_cookie(user_uid, "", expires=0)


def create_cookies(resp, username):
    from flask import request
    import datetime

    expire_date = datetime.datetime.now()
    days = 365 if (request.form.get("keepLoggedIn") == "on") else 1
    expire_date = expire_date + datetime.timedelta(days=days)
    resp.set_cookie(user, username, expires=expire_date)
    resp.set_cookie(user_uid, str(uuid.uuid4()), expires=expire_date)
