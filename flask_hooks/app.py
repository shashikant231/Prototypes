from flask import Flask, g
from time import sleep
from datetime import datetime
from users.index import users_bp

app = Flask(__name__)

app.register_blueprint(users_bp)


@app.before_request
def before_request():
    g.start = datetime.now()
    print("starting request at", g.start)
    print("Before request")


@app.after_request
def after_request(response):
    duration = datetime.now() - g.start
    print("request took", duration.total_seconds(), "seconds")
    print("After request")
    return response


@app.route("/math")
def math():
    print("sleeping ...")
    sleep(2)
    print("done sleeping")

    return "<html><body><h1>Mathematics class</h1></body></html>"


if __name__ == "__main__":
    app.run(debug=True)
