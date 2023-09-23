from flask import Flask, request, render_template
app = Flask(__name__)

POST = "POST"
GET = "GET"



@app.route("/")
def hello_world():  # put application's code here
    return "hello world"
    # return render_template("index.html")

@app.route("/profiles")
def profiles():
    return "select your profile"


@app.route("/profiles/create", methods=[GET, POST])
def save_profile():

    if request.method == POST:
        result = request.form
        return render_template("login.html", result=result)
    else:
        user = {"name": "jack", "age": 37}
        return render_template("login.html", user=user)


@app.route("/user")
def user_view():
    user = {"name": "jack", "age": 37}
    return render_template("user.html", user=user)