import uuid

register_cookie = "Seaport-User-Verified"

passw = "password"
user = "username"


def verify_is_logged_in() -> bool:
    from flask import request

    username = request.cookies.get(user)
    valid_login = request.cookies.get(register_cookie)
    if not username or not valid_login:
        return True
    return False


def create_cookies(resp, username):
    import datetime

    expire_date = datetime.datetime.now()
    expire_date = expire_date + datetime.timedelta(days=1)
    resp.set_cookie(user, username, expires=expire_date)
    resp.set_cookie(register_cookie, str(uuid.uuid4()), expires=expire_date)
