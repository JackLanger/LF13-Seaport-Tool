from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():  # put application's code here
    return "Hello World!"


@app.route("/profiles")
def profiles():
    return "select your profile"


@app.route("/profiles/create", methods=["GET", "PUT"])
def save_profile():
    data = request.data

    return data


if __name__ == "__main__":
    app.run()
